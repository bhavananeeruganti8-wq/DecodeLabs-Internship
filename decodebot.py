print("=" * 50)
print("Welcome to Rule-Based  AI chatbot 🤖")
print("Type 'HELP' to see available commands")
print("Type 'Bye'👋 to exit")
print("=" * 50)
while True:
    user=input("\n😊You:").lower().strip()
    if user in["hi","hello","hey"]:
        print("Bot🤖:Hello! Nice to meet you.")
    elif user=="how are you":
        print("Bot🤖:I'm doing great,Thanks for asking!")
    elif user=="who created you":
        print("Bot🤖: I was created using python programming")
    elif user=="what is ai":
        print("Bot🤖: AI stands for Artificial Intelligence")
    elif user=="what is python":
        print("Bot🤖: Python is popular programming language used in AI and Data science")
    elif user=="good morning":
        print("Bot🤖: Good Morning🌞! Have a Wonderful Day😃")
    elif user=="good afternoon":
        print("Bot🤖: good afternoon!")
    elif user=="good evening":
        print("Bot🤖: good evening")
    elif user=="good night":
        print("Bot🤖:Good Night🌃! Sweet Dreams💤")
    elif user=="thank you":
        print("Bot🤖: You're welcome😃")
    elif user=="help":
        print("\n Available commands:")
        print("-👋hi")
        print("-👋hello")
        print("-😊how are you")
        print("-🤖who created you")
        print("-🧠what is ai")
        print("-🐍what is python")
        print("-🌞Good Morning🌄")
        print("-☀️Good Afternoon")
        print("-🌉Good Evening")
        print("-🌝Good Night")
    elif user=="what is you name":
        print("Bot🤖:My name is DecodeBot,your Rule-Based AI Assistant")
        
    elif user=="bye":
        print("Bot🤖:Goodbye! Have a nice day😊")
        break
    else:
        print("Bot: Sorry, I don't understand 🤔that.Type 'HELP' to see available commands")
        

    
    
