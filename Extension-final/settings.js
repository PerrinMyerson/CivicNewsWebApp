document.addEventListener('DOMContentLoaded', async () => {
    // Load saved settings
    const settings = await chrome.storage.sync.get([
        'openaiApiKey',
        'transcriptApiKey',
        'darkMode'
    ]);

    // Set input values
    document.getElementById('openaiKey').value = settings.openaiApiKey || '';
    document.getElementById('transcriptKey').value = settings.transcriptApiKey || '';
    document.getElementById('darkMode').checked = settings.darkMode || false;

    // Apply dark mode if enabled
    if (settings.darkMode) {
        document.body.classList.add('dark-mode');
    }

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

    // Handle save button
    document.getElementById('saveSettings').addEventListener('click', async () => {
        const openaiApiKey = document.getElementById('openaiKey').value;
        const transcriptApiKey = document.getElementById('transcriptKey').value;
        const darkMode = document.getElementById('darkMode').checked;

        await chrome.storage.sync.set({
            openaiApiKey,
            transcriptApiKey,
            darkMode
        });

        const saveStatus = document.getElementById('saveStatus');
        saveStatus.textContent = 'Settings saved!';
        setTimeout(() => {
            saveStatus.textContent = '';
        }, 2000);
    });
}); 