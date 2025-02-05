chrome.runtime.onMessage.addListener(async (request, sender, sendResponse) => {
    if (request.action === 'createDocFromVTT') {
      sendLog("Received message to create doc from VTT.", request.tabId);
  
      try {
        chrome.webRequest.onCompleted.addListener(
          async function(details) {
            sendLog("Detected network request completion.", request.tabId);
  
            if (details.url.includes('.vtt?')) {
              sendLog(`Found .vtt file: ${details.url}`, request.tabId);
  
              try {
                // Fetch the .vtt file content
                const vttContent = await fetch(details.url).then(response => {
                  sendLog("Fetched VTT content.", request.tabId);
                  return response.text();
                });
  
                // Get the Vimeo video title for Google Doc title
                const videoTitle = await getVimeoVideoTitle(request.tabId);
                sendLog(`Video Title: ${videoTitle}`, request.tabId);
                const documentTitle = `${videoTitle} Transcript`;
  
                // Check if the document already exists in Google Drive
                const existingDocId = await checkIfDocumentExists(documentTitle);
                sendLog(`Existing Doc ID: ${existingDocId || 'None'}`, request.tabId);
  
                if (existingDocId) {
                  // Overwrite the existing document
                  sendLog("Updating existing document.", request.tabId);
                  await updateGoogleDoc(existingDocId, vttContent);
                  sendResponse({ success: true, docId: existingDocId });
                } else {
                  // Create a new document
                  sendLog("Creating new document.", request.tabId);
                  const docId = await createGoogleDoc(documentTitle, vttContent);
                  sendResponse({ success: true, docId: docId });
                }
              } catch (error) {
                sendLog(`Error during API request: ${error.message}`, request.tabId);
                sendResponse({ success: false, message: `Failed during API request: ${error.message}` });
              }
            } else {
              sendLog("No .vtt file detected in this request.", request.tabId);
            }
          },
          { urls: ["<all_urls>"] }
        );
      } catch (error) {
        sendLog(`Critical error in listener setup: ${error.message}`, request.tabId);
        sendResponse({ success: false, message: `Listener setup failed: ${error.message}` });
      }
  
      return true;  // Keep the message channel open for async responses
    }
  });
  
  // Helper function to send logs to the popup
  function sendLog(message, tabId) {
    chrome.tabs.sendMessage(tabId, { log: message });
  }
  
  // Function to get the Vimeo video title from the tab
  async function getVimeoVideoTitle(tabId) {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    sendLog(`Tab title fetched: ${tab.title}`, tabId);
    return tab.title; // Returns the tab title, assuming this matches the video title
  }
  
  // Function to get the OAuth token
  function getOAuthToken(tabId) {
    sendLog("Requesting OAuth token.", tabId);
    
    return new Promise((resolve, reject) => {
      chrome.identity.getAuthToken({ interactive: true }, (token) => {
        if (chrome.runtime.lastError || !token) {
          sendLog(`Error obtaining OAuth token: ${chrome.runtime.lastError}`, tabId);
          reject(new Error(`OAuth token error: ${chrome.runtime.lastError}`));
          return;
        }
        sendLog("OAuth token obtained.", tabId);
        resolve(token);
      });
    });
  }
  
  // Function to check if a Google Doc with the same name already exists
  async function checkIfDocumentExists(docTitle) {
    try {
      const token = await getOAuthToken();
      const response = await fetch(`https://www.googleapis.com/drive/v3/files?q=name='${docTitle}' and mimeType='application/vnd.google-apps.document'`, {
        method: 'GET',
        headers: { Authorization: `Bearer ${token}` },
      });
      
      const data = await response.json();
      sendLog(`Document search response: ${JSON.stringify(data)}`, request.tabId);
      return data.files && data.files.length > 0 ? data.files[0].id : null;
    } catch (error) {
      sendLog(`Error in document search: ${error.message}`, request.tabId);
      throw new Error(`Error in document search: ${error.message}`);
    }
  }
  
  // Function to update an existing Google Doc
  async function updateGoogleDoc(docId, content) {
    try {
      const token = await getOAuthToken();
      const request = {
        requests: [{ replaceAllText: { containsText: { text: "{{content}}", matchCase: false }, replaceText: content } }],
      };
      const response = await fetch(`https://docs.googleapis.com/v1/documents/${docId}:batchUpdate`, {
        method: 'POST',
        headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json' },
        body: JSON.stringify(request),
      });
      
      const result = await response.json();
      sendLog(`Update document response: ${JSON.stringify(result)}`, request.tabId);
    } catch (error) {
      sendLog(`Error updating document: ${error.message}`, request.tabId);
      throw new Error(`Error updating document: ${error.message}`);
    }
  }
  
  // Function to create a new Google Doc
  async function createGoogleDoc(docTitle, content) {
    try {
      const token = await getOAuthToken();
      const doc = { title: docTitle };
      const docResponse = await fetch('https://docs.googleapis.com/v1/documents', {
        method: 'POST',
        headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json' },
        body: JSON.stringify(doc),
      });
      
      const docData = await docResponse.json();
      const documentId = docData.documentId;
      sendLog(`Document created with ID: ${documentId}`, request.tabId);
      
      const insertTextRequest = {
        requests: [{ insertText: { location: { index: 1 }, text: content } }],
      };
      const updateResponse = await fetch(`https://docs.googleapis.com/v1/documents/${documentId}:batchUpdate`, {
        method: 'POST',
        headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json' },
        body: JSON.stringify(insertTextRequest),
      });
      
      const updateResult = await updateResponse.json();
      sendLog(`Document content insertion response: ${JSON.stringify(updateResult)}`, request.tabId);
      
      return documentId;
    } catch (error) {
      sendLog(`Error creating document: ${error.message}`, request.tabId);
      throw new Error(`Error creating document: ${error.message}`);
    }
  }
  