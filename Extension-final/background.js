// Initialize context menu when extension is installed or updated
chrome.runtime.onInstalled.addListener(() => {
  console.log('Extension installed/updated - creating context menu');
  // Remove existing menu items to avoid duplicates
  chrome.contextMenus.removeAll(() => {
    chrome.contextMenus.create({
      id: "generateSEO",
      title: "Generate SEO Results",
      contexts: ["selection"],
      documentUrlPatterns: ["*://*/*"]  // Include all URLs including Google Docs
    }, () => {
      if (chrome.runtime.lastError) {
        console.error('Context menu creation failed:', chrome.runtime.lastError);
      } else {
        console.log('Context menu created successfully');
      }
    });
  });
});

// Ensure content script is injected when needed
async function ensureContentScriptInjected(tabId, frameId = 0) {
    try {
        // Check if content script is already injected
        await chrome.tabs.sendMessage(tabId, { action: "ping" }, { frameId: frameId });
        console.log('Content script already active in frame:', frameId);
        return true;
    } catch (error) {
        console.log('Content script not found in frame:', frameId, 'injecting...');
        // Inject content script
        try {
            await chrome.scripting.executeScript({
                target: { tabId: tabId, frameIds: [frameId] },
                files: ['contentScript.js']
            });
            await chrome.scripting.insertCSS({
                target: { tabId: tabId, frameIds: [frameId] },
                files: ['sidebar.css']
            });
            console.log('Content script injected successfully in frame:', frameId);
            return true;
        } catch (err) {
            console.error('Failed to inject content script in frame:', frameId, err);
            return false;
        }
    }
}

// Handle context menu clicks
chrome.contextMenus.onClicked.addListener(async (info, tab) => {
    console.log('Context menu clicked!', {
        menuItemId: info.menuItemId,
        selectionText: info.selectionText,
        tabId: tab.id,
        frameId: info.frameId
    });
    
    if (info.menuItemId === "generateSEO") {
        // Ensure content script is injected before proceeding
        const frameId = info.frameId || 0;
        const isInjected = await ensureContentScriptInjected(tab.id, frameId);
        if (isInjected) {
            analyzeSEO(info.selectionText, tab.id, frameId);
        }
    }
});

// Handle transcript generation
async function generateTranscript(url) {
  try {
    // API call to transcript service would go here
    const response = await fetch('YOUR_TRANSCRIPT_API_ENDPOINT', {
      method: 'POST',
      body: JSON.stringify({ url })
    });
    const transcript = await response.json();
    
    // Store in history
    saveToHistory(url, transcript);
    
    return transcript;
  } catch (error) {
    console.error('Transcript generation failed:', error);
    return null;
  }
}

// Handle SEO analysis
async function analyzeSEO(text, tabId, frameId = 0) {
    console.log('Starting analyzeSEO', { text, tabId, frameId });
    
    try {
        // Add a small delay to ensure content script is ready
        await new Promise(resolve => setTimeout(resolve, 100));
        
        // Send message to content script in the specific frame
        console.log('Sending message to content script...');
        await chrome.tabs.sendMessage(tabId, {
            action: "displaySEOResults",
            data: text
        }, { frameId: frameId });
        console.log('Message sent successfully to content script');
    } catch (error) {
        console.error('Error in analyzeSEO:', error);
    }
}

// Save transcript to history
async function saveToHistory(url, transcript) {
  const history = await chrome.storage.local.get('transcriptHistory') || [];
  history.transcriptHistory = history.transcriptHistory || [];
  history.transcriptHistory.unshift({
    url,
    transcript,
    timestamp: new Date().toISOString()
  });
  
  // Keep only last 10 entries
  if (history.transcriptHistory.length > 10) {
    history.transcriptHistory.pop();
  }
  
  await chrome.storage.local.set({ transcriptHistory: history.transcriptHistory });
}

// Listen for theme changes
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === 'updateTheme') {
    chrome.tabs.query({}, (tabs) => {
      tabs.forEach(tab => {
        chrome.tabs.sendMessage(tab.id, {
          action: 'updateTheme',
          darkMode: message.darkMode
        }).catch(() => {
          // Ignore errors for inactive tabs
        });
      });
    });
  }
});

// Listen for tab updates to ensure content script is injected
chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (changeInfo.status === 'complete' && tab.url?.startsWith('http')) {
        // For Google Docs, we need to handle the main frame and potential iframes
        if (tab.url.includes('docs.google.com')) {
            chrome.webNavigation.getAllFrames({ tabId: tabId }, (frames) => {
                if (frames) {
                    frames.forEach(frame => {
                        ensureContentScriptInjected(tabId, frame.frameId);
                    });
                }
            });
        } else {
            ensureContentScriptInjected(tabId);
        }
    }
});

// Add these new message handlers
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === "ensureContentScript") {
        ensureContentScriptInjected(message.tabId)
            .then(result => sendResponse(result))
            .catch(error => sendResponse({ error: error.message }));
        return true;
    }
    
    if (message.action === "analyzeSEO") {
        analyzeSEO(message.text, message.tabId)
            .then(result => sendResponse(result))
            .catch(error => sendResponse({ error: error.message }));
        return true;
    }
});