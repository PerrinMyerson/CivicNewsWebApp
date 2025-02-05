document.getElementById('generate-doc').addEventListener('click', async () => {
    const logsDiv = document.getElementById('logs');
    logsDiv.innerHTML = ''; // Clear logs
  
    // Function to append logs to the popup
    function appendLog(message) {
      const logMessage = document.createElement('div');
      logMessage.textContent = message;
      logsDiv.appendChild(logMessage);
      logsDiv.scrollTop = logsDiv.scrollHeight; // Auto-scroll to bottom
    }
  
    appendLog("Starting process...");
  
    // Get the active tab info
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  
    appendLog(`Sending message to background script with tabId: ${tab.id}`);
  
    // Send a message to the background script to grab the captions and create a Google Doc
    chrome.runtime.sendMessage({ action: 'createDocFromVTT', tabId: tab.id }, (response) => {
      if (response && response.success) {
        appendLog(`Google Doc created successfully! Document ID: ${response.docId}`);
      } else if (response && response.message) {
        appendLog(`Failed to create Google Doc: ${response.message}`);
      } else {
        appendLog('No response from the background script.');
      }
    });
  });
  
  // Listen for logs from the background script
  chrome.runtime.onMessage.addListener((message) => {
    if (message.log) {
      const logsDiv = document.getElementById('logs');
      const logMessage = document.createElement('div');
      logMessage.textContent = message.log;
      logsDiv.appendChild(logMessage);
      logsDiv.scrollTop = logsDiv.scrollHeight; // Auto-scroll to bottom
    }
  });
  