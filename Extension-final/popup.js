document.addEventListener('DOMContentLoaded', async () => {
    const analyzeClipboard = document.getElementById('analyzeClipboard');
    const showManualInput = document.getElementById('showManualInput');
    const manualInputSection = document.getElementById('manualInputSection');
    const manualText = document.getElementById('manualText');
    const analyzeManual = document.getElementById('analyzeManual');
    const toggleSettings = document.getElementById('toggleSettings');
    const settingsSection = document.getElementById('settingsSection');
    const saveSettings = document.getElementById('saveSettings');
    const saveStatus = document.getElementById('saveStatus');

    // Load saved settings
    const settings = await chrome.storage.sync.get([
        'openaiApiKey',
        'transcriptApiKey',
        'darkMode'
    ]);

    // Set input values and apply dark mode
    document.getElementById('openaiKey').value = settings.openaiApiKey || '';
    document.getElementById('transcriptKey').value = settings.transcriptApiKey || '';
    document.getElementById('darkMode').checked = settings.darkMode || false;
    
    // Apply dark mode if enabled
    if (settings.darkMode) {
        document.body.classList.add('dark-mode');
    }

    // Handle clipboard analysis
    analyzeClipboard.addEventListener('click', async () => {
        try {
            const text = await navigator.clipboard.readText();
            if (text) {
                const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
                analyzeSEOText(text, tab.id);
            } else {
                alert('No text found in clipboard!');
            }
        } catch (error) {
            console.error('Clipboard access error:', error);
            alert('Unable to access clipboard');
        }
    });

    // Toggle manual input section
    showManualInput.addEventListener('click', () => {
        manualInputSection.classList.toggle('active');
        settingsSection.classList.remove('active');
    });

    // Toggle settings section
    toggleSettings.addEventListener('click', () => {
        settingsSection.classList.toggle('active');
        manualInputSection.classList.remove('active');
    });

    // Handle manual text analysis
    analyzeManual.addEventListener('click', async () => {
        const text = manualText.value.trim();
        if (text) {
            const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
            analyzeSEOText(text, tab.id);
        } else {
            alert('Please enter some text to analyze!');
        }
    });

    // Handle dark mode toggle
    document.getElementById('darkMode').addEventListener('change', async (e) => {
        const isDarkMode = e.target.checked;
        document.body.classList.toggle('dark-mode', isDarkMode);
        await chrome.storage.sync.set({ darkMode: isDarkMode });
        
        // Send message to update all extension pages
        chrome.runtime.sendMessage({ 
            action: 'updateTheme', 
            darkMode: isDarkMode 
        });
    });

    // Handle settings save
    saveSettings.addEventListener('click', async () => {
        const openaiApiKey = document.getElementById('openaiKey').value;
        const transcriptApiKey = document.getElementById('transcriptKey').value;
        const darkMode = document.getElementById('darkMode').checked;

        await chrome.storage.sync.set({
            openaiApiKey,
            transcriptApiKey,
            darkMode
        });

        saveStatus.style.display = 'block';
        setTimeout(() => {
            saveStatus.style.display = 'none';
        }, 2000);
    });
});

async function analyzeSEOText(text, tabId) {
    try {
        // Ensure content script is injected
        await chrome.runtime.sendMessage({
            action: "ensureContentScript",
            tabId: tabId
        });

        // Send the analysis request
        await chrome.runtime.sendMessage({
            action: "analyzeSEO",
            text: text,
            tabId: tabId
        });

        // Close the popup
        window.close();
    } catch (error) {
        console.error('Analysis error:', error);
        alert('Error analyzing text. Please try again.');
    }
} 