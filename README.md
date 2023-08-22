# Savvy Service telegram bot

This is a Django project that implements a task management system. The project aims to provide a 
user-friendly interface for managing tasks and workers within an organization. 
It allows users to efficiently track and manage tasks, assign them to workers, and monitor their progress. 
By using this task management system, organizations can improve their productivity and ensure 
effective task allocation and completion.

## Installing / Getting started

A quick introduction of the minimal setup you need to get this telegram bot up &
running.

```shell
git clone https://github.com/IvanKorshunovE/savvy_service
cd savvy_service
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Execute the command `ngrok http 8000` to configure the port from 
the Telegram bot to your local machine and copy the url address from the terminal 
to WEB_HOOK_URL in your .env file
Create a `.env` file by copying the `.env.sample` file and 
populate it with the required values
python manage.py runserver # starts Django Server
```

After executing these commands, the Django server should be up and running, 
allowing you to access and interact with the telegram bot.

## Features

The Expense Tracker Telegram Bot helps you manage your expenses easily. 
Here are some of its features:

## Start Command

Use the `/start` command to begin using the bot. It will provide you with 
instructions on how to enter your expenses.

## Help Command

If you need assistance with using the bot, just type `/help`. 
It will provide you with guidance on entering expenses.

## Get Expenses Command

To get the total amount of your expenses, use the `/get_expenses` command. 
The bot will display the total amount in Ukrainian hryvnias.

## Adding Expenses

You can add your expenses by sending the amount and a short 
description separated by spaces. The bot will save this information.
