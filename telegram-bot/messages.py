# create the logic for fetching the required things for creating messages for users

# replies = {
#     "/start_new_user": "Hello welcome to iitm bs bot. use /select to select the year in which u are, thanks",
#     "/start_old_user": "Hello welcome back to iitm bs bot. thanks",
#     "/select": "Give me the year in which you are",
#     "inform_active_bot":"Hello Admin , I am active now "
# }


replies = {
    "/help": "🌟 Hello there! Need a helping hand? 🤝 I'm here to guide you through your IIT Madras BSc journey! As your friendly educational chatbot, my mission is to make accessing resources and information as easy as pie 📚🤓. Whether you're looking for course materials, schedule details, or any other academic support, just type in your query and consider it sorted! How can I assist you today? 🎓💡",

    "/start_new_user": "🎉 Welcome aboard the IIT Madras BSc adventure! 🚀 To get started, could you please register? It's a quick and easy process that will unlock a world of resources tailored just for you! 📚✨ Just click the 'Register' button below and fill in your details. Once you're all set, you'll be ready to dive into a sea of learning and discovery! 🌊🎓 Can't wait to see you on the inside! 🙌 \nCan you tell me in which level you are?",

    "/start_old_user": "🌟 Welcome back! 🚀 It's great to see you again on your IIT Madras BSc journey. We've missed you! Ready to explore more amazing learning resources and tools? 📚💡 Just type in what you're looking for, and I'll help you navigate to it in no time. Let's continue this exciting educational adventure together! 🎓✨ Use the following commands :\n/notes = for accessing notes \n/pyqs = for accessing pyqs \n" , 

    "/todays_deadlines": """📅 Good day! Here are your deadlines for today: 🚀
[list_of_deadlines]
📝 Remember, a well-planned study schedule is key to success! If you need any help or resources to complete these assignments, just let me know. I'm here to help you stay on track and ace those deadlines! 🎯📚""",

    "/update_selected_subjects": """📚 Time for an update! Are you taking new subjects this term? Let's make sure your subject list is up-to-date so I can provide you with the most relevant information and resources. 🌟
👉 To update your subjects, please follow these steps:
* 		Click on the 'Update Subjects' button below.
* 		Select the subjects you're taking this term.
* 		Confirm your selection.
Once you're done, I'll tailor my assistance to match your current subjects! 🎓✨ Need any help along the way? Just ask!
[Update Subjects Button]""",

    "/thanks": """🌟 Thank you for spending time with us today! Your dedication to your studies at IIT Madras BSc is truly inspiring. 🎓 Remember, I'm always here to help you with any academic resources or guidance you might need. 📚💡
Have a wonderful day ahead, and don't hesitate to return whenever you need assistance or just want to explore more learning opportunities. Until next time, keep up the great work! 👋🌈""", 

    "/about" : """🌐 About This Project & Bot 🤖
Welcome to your friendly educational companion for the IIT Madras BSc degree program! 🎓 This chatbot is designed to streamline your learning experience by providing easy access to academic resources, information on course schedules, assignment deadlines, and much more. 📚✨
Created with the goal of enhancing student engagement and success, this bot is more than just a tool - it's your personal academic assistant, always ready to assist with your queries and guide you through your educational journey at IIT Madras. 🚀
Whether you're a new student or returning for another term, I'm here to make your academic life easier and more productive. So, how can I help you today? 🌟""", 

    "/suggest_improvements": """🤖 We're on a mission to make your educational journey smoother and more enjoyable, and your feedback is crucial! 🌟 Do you have any suggestions on how we can improve? 🛠️
Whether it's about adding new features, enhancing existing ones, or just tweaking the way we communicate, every piece of feedback helps us grow and serve you better. 🌱
Please click the 'Feedback' button below to share your thoughts. Your input is invaluable in helping us create the best possible experience for you and your fellow learners. Thank you for being a part of our continuous improvement journey! 🙌
[Feedback Button]""",

    "/found_bug": """🐞 Oops! Encountered a glitch? We're here to fix it! Your help in identifying bugs is super important to keep everything running smoothly. 🛠️
Please click the 'Report Bug' button below to tell us more about the issue you've found. The more details you can provide, the quicker we can squash that bug and improve your experience. 🕵️‍♀️
We appreciate your patience and assistance in making this chatbot better for everyone. Thank you for being a vigilant member of our community! 🌟
[Report Bug Button]""",

    "/maintainer_login": """🔐 Welcome, Maintainer! 👋 It's time to dive into the backend of our educational chatbot. Your expertise keeps this system running smoothly and efficiently for our users. 🚀
Please enter your credentials to access the maintenance panel. Here, you can update, troubleshoot, and enhance the bot to ensure the best possible experience for our learners. 🛠️📚
Your work behind the scenes is greatly appreciated – together, we're making a real difference in the educational journey of countless students! 🌟
[Login Credentials Input]""",

"/admin_login": """🔐 Welcome, Admin! 👋 It's time to dive into the backend of our educational chatbot. Your expertise keeps this system running smoothly and efficiently for our users. 🚀
Please enter your credentials to access the Admin panel. Here, you can update, troubleshoot, and enhance the bot to ensure the best possible experience for our learners. 🛠️📚
Your work behind the scenes is greatly appreciated together, we're making a real difference in the educational journey of countless students! 🌟
[Login Credentials Input]""",

"/user_not_registered": """🚨 It looks like your registration isn't complete yet! To fully unlock all the resources and features of this educational chatbot, we need you to finish signing up. 📝🔑
Registration is quick and easy – and it opens the door to a wealth of tailored academic resources and support for your IIT Madras BSc journey. 🎓✨
Please click on the 'Complete Registration' button below to get started. If you need any help or have questions during the process, feel free to reach out. We're here to ensure a smooth and efficient setup for you! 🌟
[Complete Registration Button]""",

"/user_not_authorize_for_command": """🚫 Sorry, it seems like you don't have the authorization to access this command. This feature is restricted to specific user roles or access levels. 🛑
If you believe this is a mistake or if you need access to this feature for your academic needs, please reach out to us. We're here to help you get the right access and ensure you have everything you need for your educational journey at IIT Madras BSc. 🎓✨
For any other queries or assistance, feel free to ask. Your success is our top priority! 🌟""",

"/notes" : """📓 Looking for notes? You've come to the right place! To help you find exactly what you need, could you please specify which subject's notes you're interested in? 🤔📚
Just type the name of the subject below, and I'll fetch the latest and most relevant notes for you. Whether it's Mathematics, Physics, Computer Science, or any other subject from your IIT Madras BSc curriculum, I've got you covered! 🎓✨
[Subject Input Field]
Your academic success is our goal, and having the right notes can make all the difference. Let's get studying! 🌟""",

"/notes_of_selected_subject": """📚 Here are the notes for [subject_name]! Dive into a world of knowledge and insights tailored just for your studies. 🎓✨
[Notes]
Whether you're revising for exams, brushing up on concepts, or just exploring new topics, these notes are designed to help you excel. 🌟 Remember, if you need more resources or have any questions, I'm here to assist you every step of the way!
Keep up the great work, and happy studying! 📖🚀""",

"/pyqs": """📚 Looking for Previous Year's Question Papers (PYQs)? You're in the right place! These papers can be a great resource to prepare for your exams. 🎓✏️
To help you find exactly what you need, could you please specify the subject you're interested in? Just type in the subject name or choose from the list below, and I'll fetch the PYQs for you. 📃🔍
Whether it's Mathematics, Physics, Computer Science, or any other subject you're studying, I've got you covered with a comprehensive archive of past papers. 🌟
[Subject Selection Options]""",

"/pyqs_of_selected_subject": """📄 Here are the Previous Year's Question Papers (PYQs) for [subject_name]! These are a fantastic resource to understand the exam pattern and to test your knowledge. 🎯📚
[PYQS]
Use these papers to practice and refine your understanding of the subject. They're a great way to gauge your preparedness and identify areas where you might need a bit more focus. 🤓
If you need any more assistance or resources, just let me know. I'm here to support you in acing [subject_name]! 🌟
Happy studying and all the best for your exams! 🚀"""



}