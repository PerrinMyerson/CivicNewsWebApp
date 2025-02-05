// Immediately inject a flag to show the script is loaded
console.log('Content script loaded at:', new Date().toISOString());

// Create and inject sidebar
function createSidebar() {
    console.log('Creating sidebar...');
    const sidebar = document.createElement('div');
    sidebar.id = 'seo-analyzer-sidebar';
    
    // Get dark mode preference
    chrome.storage.sync.get('darkMode', ({ darkMode }) => {
        const isDarkMode = darkMode || false;
        const backgroundColor = isDarkMode ? '#2d2d2d' : 'white';
        const textColor = isDarkMode ? '#ffffff' : '#333333';
        const headerBgColor = isDarkMode ? '#1a1a1a' : '#f5f5f5';
        const borderColor = isDarkMode ? '#444444' : '#dddddd';
        
        sidebar.innerHTML = `
            <div class="sidebar-header">
                <h3>SEO Analysis Results</h3>
                <button class="close-sidebar">×</button>
            </div>
            <div class="sidebar-content"></div>
        `;
        
        // Apply consistent styling
        sidebar.style.cssText = `
            position: fixed !important;
            top: 0 !important;
            right: 0 !important;
            width: 300px !important;
            height: 100vh !important;
            background: ${backgroundColor} !important;
            color: ${textColor} !important;
            z-index: 2147483647 !important;
            display: none;
            box-shadow: -2px 0 5px rgba(0,0,0,0.2) !important;
            font-family: Arial, sans-serif !important;
        `;
        
        const header = sidebar.querySelector('.sidebar-header');
        header.style.cssText = `
            padding: 15px !important;
            background: ${headerBgColor} !important;
            border-bottom: 1px solid ${borderColor} !important;
            display: flex !important;
            justify-content: space-between !important;
            align-items: center !important;
            margin: 0 !important;
        `;
        
        const headerTitle = header.querySelector('h3');
        headerTitle.style.cssText = `
            margin: 0 !important;
            color: ${textColor} !important;
            font-size: 16px !important;
            font-weight: bold !important;
        `;
        
        const closeButton = header.querySelector('.close-sidebar');
        closeButton.style.cssText = `
            border: none !important;
            background: none !important;
            color: ${textColor} !important;
            font-size: 24px !important;
            cursor: pointer !important;
            padding: 0 10px !important;
        `;
        
        const content = sidebar.querySelector('.sidebar-content');
        content.style.cssText = `
            padding: 15px !important;
            color: ${textColor} !important;
        `;
    });
    
    document.body.appendChild(sidebar);
    
    // Add close button listener
    sidebar.querySelector('.close-sidebar').addEventListener('click', () => {
        sidebar.style.display = 'none';
    });
    
    return sidebar;
}

// Handle messages from background script
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === "ping") {
        sendResponse({ status: "alive" });
        return true;
    }
    
    if (message.action === "displaySEOResults") {
        let sidebar = document.getElementById('seo-analyzer-sidebar');
        
        if (!sidebar) {
            sidebar = createSidebar();
        }
        
        chrome.storage.sync.get('darkMode', ({ darkMode }) => {
            const isDarkMode = darkMode || false;
            const backgroundColor = isDarkMode ? '#2d2d2d' : 'white';
            const textColor = isDarkMode ? '#ffffff' : '#333333';
            
            sidebar.style.display = 'block';
            const content = sidebar.querySelector('.sidebar-content');
            
            // Sanitize the text
            const sanitizedText = message.data
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .trim();
            
            content.innerHTML = `
                <div class="selected-text">
                    <h4 style="
                        color: ${textColor} !important;
                        margin: 0 0 10px 0 !important;
                        font-size: 14px !important;
                        font-weight: bold !important;
                    ">Selected Text:</h4>
                    <div class="text-content" style="
                        color: ${textColor} !important;
                        font-family: Arial, sans-serif !important;
                        font-size: 14px !important;
                        line-height: 1.5 !important;
                        white-space: pre-wrap !important;
                        word-wrap: break-word !important;
                        padding: 10px !important;
                        background-color: ${backgroundColor} !important;
                        border-radius: 4px !important;
                    ">${sanitizedText}</div>
                </div>
            `;
        });
        
        sendResponse({ status: 'Sidebar displayed successfully' });
    }
    
    return true;
});

// Listen for theme changes
chrome.runtime.onMessage.addListener((message) => {
    if (message.action === 'updateTheme') {
        const sidebar = document.getElementById('seo-analyzer-sidebar');
        if (sidebar) {
            sidebar.remove();
            createSidebar();
        }
    }
});

// Inject a test element to verify the script is running
const testElement = document.createElement('div');
testElement.id = 'seo-analyzer-test';
testElement.style.display = 'none';
document.body.appendChild(testElement);
console.log('Test element injected');