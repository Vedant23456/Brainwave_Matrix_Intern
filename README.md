Mechanisms Used:
Regex Pattern Matching: By utilizing advanced regular expressions, the tool can identify suspicious patterns within URLs that are commonly used in phishing attempts.
Domain Analysis: This involves checking the domain structure to detect anomalies or inconsistencies that might indicate a phishing attempt. For instance, phishing URLs often use misleading domain names that appear legitimate at first glance.
IP Address Detection: Phishing links often use IP addresses instead of domain names to bypass security filters. This tool can flag such URLs, adding an extra layer of scrutiny.

💡 Current Status:
The project is still in its intermediate stages, and the backend is yet to be created. However, the foundational work on the URL detection mechanism is well underway. The goal is to develop a robust and reliable phishing link scanner that can be integrated into various applications and systems to enhance cybersecurity.

Libraries Used:
The project leverages several essential libraries, including Flask for web development, regular expressions (re module) for pattern matching, and urllib.parse for URL parsing.
