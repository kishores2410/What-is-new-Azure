# What's New in Azure

This project, "What's New in Azure", serves as an automated news updater for Azure services. It's designed to help developers, IT professionals, or anyone interested in Azure stay updated with the latest changes, updates, or announcements from Azure.

The project uses a Python Azure Function that is triggered every 12 hours. It fetches updates from the Azure feed and posts them on Twitter, allowing followers on Twitter (X) to get timely updates about Azure.

## Connect on Twitter

For more updates and information on Azure Services, follow on Twitter (X): [What is new in Azure](https://x.com/WhatsNewInAzure)

## This can be particularly useful for:

- Developers who use Azure services and want to stay informed about updates or changes that could affect their work.
- IT professionals who need to keep track of Azure updates for managing their organization's cloud infrastructure.
Azure enthusiasts who want to stay in the loop about the latest Azure news and updates.
- By automating this process, the project saves users the time and effort of manually checking for updates, and ensures that they don't miss out on important Azure news.


## Project Structure

- `.env.example`: Contains environment variables such as the Azure feed URL, connection string for Azure Data Tables, and Twitter API keys.
- `azure_client.py`: Contains the Azure client code.
- `config.py`: Contains the configuration code.
- `feed_processor.py`: Contains the main function that processes the Azure feed.
- `function_app.py`: Contains the Azure Function App code.
- `twitter_client.py`: Contains the Twitter client code.
- `azure-resource-manager-template.json`: Contains the Azure Resource Manager (ARM) template for deploying the resources needed for this project.
- `.vscode/tasks.json`: Contains tasks for running the function app locally and installing the required Python packages.
- `requirements.txt`: Contains the Python packages required for this project.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6 or higher
- Azure Functions Core Tools
- An Azure account with an active subscription
- Twitter Developer account

# How to Write and Deploy an Azure Function

Follow these steps to write and deploy an Azure Function:

1. **Create a New Azure Function Project**: Use Azure Functions Core Tools or Azure portal to create a new Azure Function project.
2. **Write Your Function**: Write your function code in a Python file within your project directory.
3. **Install Dependencies**: If your function requires any dependencies, ensure they are listed in `requirements.txt`.
4. **Test Locally**: Test your function locally using Azure Functions Core Tools.
5. **Deploy to Azure**: Deploy your function to Azure using Azure Functions Core Tools or directly from Visual Studio Code.
6. **Monitor and Manage**: Monitor and manage your deployed function through the Azure portal or using Azure CLI.

## Future Improvements

Here are some enhancements that could be made to the project in the future:

1. **Include More Feeds**: Expand the scope of the project by including more feeds. This could include links to events, exams, and other relevant Azure resources.
2. **Use AI for Message Generation**: Implement an AI model to generate the update messages. This could make the messages more informative and engaging, and could also allow for customization based on the user's preferences or past interactions.
