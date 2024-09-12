import aiml
kernel=aiml.Kernel()
kernel.learn("C:/Users/admin/Desktop/basic_chat.aiml")
#kernel.respond("LOAD")
while True:
    print(kernel.respond(input("Enter your message >>")))
