
# 📰 Daily News Email Automation

Welcome to the **Daily News Email Automation** project! This repository hosts a Python-based solution for fetching the latest popular and newest news articles from [Onet Wiadomości](https://wiadomosci.onet.pl/) and sending them via email to a list of recipients every day at 21:00 CEST. The solution leverages GitHub Actions for scheduling and automating the daily email dispatch.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- 🌐 **Fetch Latest News**: Scrapes the latest popular and newest news articles from Onet Wiadomości.
- ✉️ **Email Notifications**: Sends daily email notifications with the latest news articles.
- 🕒 **Automated Schedule**: Uses GitHub Actions to schedule the email dispatch at 21:00 CEST every day.
- 📸 **Embedded Images**: Ensures images in the articles are embedded and displayed correctly in the email.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 or higher
- GitHub account
- SMTP server credentials (for sending emails)

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/news_by_email.git
    cd news_by_email
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up GitHub Secrets**:
   
   - Go to your GitHub repository.
   - Navigate to `Settings > Secrets and variables > Actions`.
   - Add the following secrets:
     - `EMAIL_USER`: Your email address.
     - `EMAIL_PASS`: Your email password.
     - `RECIPIENT_EMAILS`: Comma-separated list of recipient emails.

## Usage
    
**Deploy to GitHub Actions**:

    - Commit and push your changes to the GitHub repository:
      ```bash
      git add .
      git commit -m "Initial commit"
      git push origin main
      ```

    - GitHub Actions will automatically pick up the workflow file and schedule the job to run daily at 21:00 CEST.

## Project Structure

```plaintext
news_by_email/
├── .github/
│   └── workflows/
│       └── main.yml       # GitHub Actions workflow file
├── email_content.py       # Email content creation and image embedding
├── extract.py             # News extraction logic
├── fetch.py               # Web scraping utility
├── main.py                # Main script for GitHub Actions
├── requirements.txt       # Python dependencies
```

## Contributing

Contributions are welcome! To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

Please ensure your code adheres to the existing code style and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Onet Wiadomości](https://wiadomosci.onet.pl/) for providing the news content.
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) for web scraping.
- [GitHub Actions](https://github.com/features/actions) for CI/CD automation.

---

Thank you for using **Daily News Email Automation**! If you have any questions or need further assistance, feel free to open an issue or contact the project maintainers.

Happy coding! 🚀
