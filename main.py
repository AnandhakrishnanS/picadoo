from typing import Final
import random

from pyexpat.errors import messages
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '7332723318:AAG_l3ymUpGwqrH8jSL5wpP_7LVLhlHFzBY'
BOT_USERNAME: Final = '@picadoobot'


# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
 await update.message.reply_text(
  "Hello, do you want to pick:\n"
  "[1] Room cleaners\n"
  "[2] Bathroom cleaner\n"
  "[3] Both room and bathroom cleaners\n"
  "Pick a number"
 )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
 await update.message.reply_text(
  "I will pick who will be the next room or bathroom cleaner. "
  "Just choose one of the commands, and I will display the selected names."
 )


async def remove_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
 await update.message.reply_text("OK, send me the name of the person you want to remove.")


# Data
room_clean = ['Anandhu', 'Nithin', 'Nikhil', 'Ritto', 'Joel', 'Vysav', 'Aqsam', 'Unais']
bathroom_clean = ['Anandhu', 'Nithin', 'Nikhil', 'Ritto', 'Joel', 'Vysav', 'Aqsam', 'Unais']


# Handle responses
def handle_response(option: int) -> str:
 global room_clean
 global bathroom_clean

 if option == "1":
  x = ''
  for _ in range(2):
   if len(room_clean) == 0:
    room_clean = ['Anandhu', 'Nithin', 'Nikhil', 'Ritto', 'Joel', 'Vysav', 'Aqsam', 'Unais']
    selected = random.choice(room_clean)
    room_clean.remove(selected)
    x += selected + ' '
   else:
    selected = random.choice(room_clean)
    room_clean.remove(selected)
    x += selected + ' '
  return "Room cleaning: "+ x.strip()



 elif option == "2":  # Picking for bathroom cleaning
  x = ''
  if len(bathroom_clean) == 0:
   bathroom_clean = ['Anandhu', 'Nithin', 'Nikhil', 'Ritto', 'Joel', 'Vysav', 'Aqsam', 'Unais']
   selected = random.choice(bathroom_clean)
   bathroom_clean.remove(selected)
   x += selected + ' '
  else:
   selected = random.choice(bathroom_clean)
   room_clean.remove(selected)
   x += selected + ' '
 return "Bathroom cleaning: "+ x.strip()

 elif option == "3":  # Picking for both room and bathroom cleaning
  x = ''
  if len(bathroom_clean) == 0:
   bathroom_clean = ['Anandhu', 'Nithin', 'Nikhil', 'Ritto', 'Joel', 'Vysav', 'Aqsam', 'Unais']
   selected = random.choice(bathroom_clean)
   bathroom_clean.remove(selected)
   x += selected + ' '
  else:
   selected = random.choice(bathroom_clean)
   room_clean.remove(selected)
   x += selected + ' '
  t: str ="Bathroom cleaning: " + x.strip()
  j = ''
  for _ in range(2):
   if len(room_clean) == 0:
    room_clean = ['Anandhu', 'Nithin', 'Nikhil', 'Ritto', 'Joel', 'Vysav', 'Aqsam', 'Unais']
    selected = random.choice(room_clean)
    room_clean.remove(selected)
    j += selected + ' '
   else:
    selected = random.choice(room_clean)
    room_clean.remove(selected)
    j += selected + ' '
   l:str ="  Room cleaning: "+ j.strip()
   return "option 3 is in maintenance please use other options😊"

 return "Invalid option. Please provide a valid input."
async def handle_message(update:Update,context:ContextTypes.DEFAULT_TYPE):
 message_type:str = update.message.chat.type
 text:str= update.message.text
 print(f'user({update.message.chat.id}) in {message_type}: "{text}"')
 if message_type == 'group':
  if BOT_USERNAME in text:
   new_text:str = text.replace(BOT_USERNAME,'').strip()
   response:str = handle_response(new_text)
  else:
   return
 else:
  response:str = handle_response(text)
 print('Bot:',response)
 print(bathroom_clean)
 await update.message.reply_text(response)

async def error(update:Update,context:ContextTypes.DEFAULT_TYPE):
 print(f'Updat{update} caused error {context.error}')
 print(len(bathroom_clean))

if __name__ == '__main__':
 print("BOT booting")
 app = Application.builder().token(TOKEN).build()
 app.add_handler(CommandHandler('Start', start_command))
 app.add_handler(CommandHandler('help', help_command))
 app.add_handler(CommandHandler('remove', remove_command))

 # messages
 app.add_handler(MessageHandler(filters.TEXT, handle_message))

 # errors
 app.add_error_handler(error)
 print("<<<polling >>>")
 app.run_polling()


