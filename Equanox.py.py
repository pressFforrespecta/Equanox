import time

a = input("Enter your name: ")

# Asking for age and ensuring it's a valid number
while True:
    try:
        b = int(input("Enter your age: "))
        break
    except ValueError:
        print("Please enter a valid number for age.")

c = input("Enter your hobbies: ")
d = input("What are you stressed about? ").lower()  # Convert to lowercase for consistency

# Stressor-based advice for general categories
def give_advice(d):
    if d == "studies":
        print("Stress due to studies can be managed by breaking your study sessions into chunks of time, ensuring you take regular breaks, and getting enough sleep. Try using study techniques like spaced repetition, and don’t hesitate to ask for help if needed.")
    elif d == "exams":
        print("Exam stress is common. Prepare early by making a study plan, practicing past papers, and ensuring you’re well-rested. During exams, stay calm, focus on breathing exercises, and avoid cramming the night before.")
    elif d == "work":
        print("Work-related stress can accumulate over time. Focus on maintaining a healthy work-life balance, setting realistic goals, and learning to delegate. Daily mindfulness exercises can also help reduce anxiety related to work pressure.")
    elif d == "financial problems":
        print("Financial stress can be overwhelming. Start by creating a budget and sticking to it. Focus on reducing unnecessary expenses, and consider speaking to a financial advisor for long-term solutions. Avoid letting finances take over your mental health.")
    elif d == "job insecurity":
        print("Job insecurity can cause anxiety. Stay proactive by updating your resume, networking, and learning new skills. Take time to focus on things you can control and prioritize self-care during periods of uncertainty.")
    elif d == "family issues":
        print("Family stress can take a toll on your mental health. Open and honest communication is key. If the issues persist, consider family therapy. Make time for self-care and personal space when family dynamics become overwhelming.")
    elif d == "relationship problems":
        print("Relationship stress is natural, but communication is essential. Schedule time to discuss issues calmly. Consider couples counseling if needed, and remember that setting boundaries is okay.")
    elif d == "marital stress":
        print("Marriage can sometimes become a source of stress. Ensure you and your partner prioritize communication and work together to resolve conflicts. Consider seeking professional counseling to better understand and strengthen your relationship.")
    elif d == "divorce":
        print("Divorce can be one of the most challenging life events. Focus on emotional healing, seeking legal advice, and surrounding yourself with supportive friends or family. Take the time to rediscover your personal goals and priorities post-divorce.")
    elif d == "parenting stress":
        print("Parenting stress is very common. Set realistic expectations for yourself as a parent, create a routine, and don’t hesitate to ask for help from family or parenting groups. Make sure to carve out time for self-care, even if it’s just a few minutes each day.")
    elif d == "childcare":
        print("Childcare challenges can add to your stress levels. Research childcare options, set up a support network of friends or family, and organize your day to include downtime for yourself.")
    elif d == "health concerns":
        print("Health-related stress can weigh heavily on your mind. Ensure you are attending regular check-ups, maintaining a balanced diet, exercising, and seeking medical attention as needed. Mental well-being is equally important, so don’t hesitate to talk to a therapist if your health concerns are overwhelming.")
    elif d == "chronic illness":
        print("Living with a chronic illness can create ongoing stress. Focus on building a strong support system, both emotionally and medically. Engage in activities that promote mental well-being, and practice self-compassion.")
    elif d == "mental health":
        print("Mental health is essential for overall well-being. Practice daily mindfulness, engage in physical activity, and make sure you seek therapy or counseling when needed. Regular check-ins with yourself can help track your mental health and identify when professional support is necessary.")
    elif d == "anxiety":
        print("Anxiety can be debilitating. Practice breathing exercises, mindfulness, and consider cognitive behavioral therapy (CBT) to manage your symptoms. Exercise regularly to help reduce anxiety, and avoid caffeine if it tends to worsen your symptoms.")
    elif d == "depression":
        print("Depression can feel isolating, but reaching out for support is critical. Engage in activities that bring you joy, even if they seem difficult at first. Speak to a healthcare provider about therapy or medication options if needed.")
    elif d == "social anxiety":
        print("Social anxiety can prevent you from engaging in social activities. Start by practicing in low-pressure situations, and consider therapy to develop coping strategies. Remember that most people are focused on themselves, not judging you.")
    elif d == "loneliness":
        print("Loneliness can be difficult. Try to connect with others by joining clubs, volunteering, or simply reaching out to old friends. Remember, building new relationships takes time, so be patient and kind to yourself.")
    elif d == "bereavement":
        print("Grief is a natural response to losing a loved one. Allow yourself time to process emotions, talk to a counselor if needed, and focus on remembering the good memories. Surround yourself with a support system during the grieving process.")
    elif d == "grief":
        print("Grieving is a journey, and everyone experiences it differently. It’s important to give yourself space to mourn and to lean on your support system when needed. If grief feels overwhelming, consider talking to a grief counselor.")
    elif d == "burnout":
        print("Burnout occurs when you've been pushing yourself too hard for too long. To prevent burnout, schedule regular breaks, set boundaries between work and personal time, and engage in activities that help you relax and recharge.")
    elif d == "overworking":
        print("Overworking leads to burnout. Set clear boundaries for your workday, make time for hobbies, and prioritize downtime. Engaging in stress-reducing activities such as meditation or exercise can help you maintain balance.")
    elif d == "climate change":
        print("Climate change concerns are valid. Focus on the actions you can take to contribute to environmental solutions, such as reducing waste, supporting sustainable practices, and engaging in local community efforts. Connect with others who share your concerns to feel empowered.")
    elif d == "aging":
        print("Aging comes with its own set of challenges, but staying active, engaging your mind, and maintaining social connections can help. Focus on maintaining a healthy lifestyle, both physically and mentally.")
    elif d == "retirement":
        print("Retirement can bring uncertainty. Focus on planning activities that keep you engaged and active, and consider part-time work or volunteering to maintain a sense of purpose. Connect with others who are going through the same phase of life.")
    elif d == "career change":
        print("Changing careers can feel daunting. Break down your goals into small, actionable steps, seek guidance from mentors, and be patient with yourself as you adapt to the new direction.")
    elif d == "uncertainty":
        print("Uncertainty is a natural part of life. Focus on grounding yourself in the present through mindfulness and meditation. Make a list of things you can control, and try to let go of the rest.")
    elif d == "fear of failure":
        print("Fear of failure is common, but it's important to reframe failure as an opportunity for growth. Focus on learning from your mistakes rather than fearing them. Remember, progress is more important than perfection.")
    elif d == "perfectionism":
        print("Perfectionism can be exhausting. Practice self-compassion and focus on the effort you’re putting in rather than achieving perfect results. Learn to celebrate your progress and growth along the way.")
    elif d == "public speaking":
        print("Public speaking is a common fear. Prepare well, practice in small settings, and take deep breaths to calm nerves before speaking. Remember, the audience is there to learn, not to judge.")
    elif d == "identity crisis":
        print("An identity crisis can be unsettling. Take time to reflect on your values and what truly matters to you. Talk to a trusted mentor or counselor to help you navigate this phase of self-discovery.")
    elif d == "sleep problems":
        print("Sleep issues can affect all aspects of your life. Establish a nighttime routine, limit screen time before bed, and ensure your sleeping environment is comfortable. Consider relaxation techniques like meditation or deep breathing before sleep.")
    elif d == "insomnia":
        print("Insomnia can be frustrating. Practice sleep hygiene by going to bed and waking up at the same time each day, avoiding caffeine, and creating a comfortable sleep environment.")

    # Dedicated section for various addictions
    elif d == "addiction":
        print("Addiction is difficult to overcome, but recovery is possible. Seek professional help, join support groups, and stay connected with loved ones who support your journey to recovery.")
    elif d == "smoking":
        print("Smoking addiction can be challenging, but quitting is one of the best things you can do for your health. Consider nicotine replacement therapy, seek support from a counselor, and use stress-management techniques to reduce cravings.")
    elif d == "alcohol":
        print("Alcohol addiction can be managed through support groups such as Alcoholics Anonymous, counseling, and reducing triggers in your environment. Focus on developing healthier coping mechanisms and staying accountable to a support network.")
    elif d == "drug addiction":
        print("Drug addiction requires professional help, including therapy and rehabilitation. Seek out recovery programs, join support groups, and focus on building a strong support system for the road ahead.")
    elif d == "technology":
        print("Technology addiction can disconnect you from real-life experiences. Set limits for screen time, schedule offline activities, and consider using apps that help manage your digital habits.")
    elif d == "social media":
        print("Social media addiction can negatively impact mental health. Set boundaries for your screen time, schedule digital detoxes, and focus on connecting with people in person.")
    elif d == "video games":
        print("Video game addiction can lead to neglecting other important areas of life. Set time limits on gaming, explore other hobbies, and consider seeking professional help if the addiction is impacting your daily life.")
    elif d == "gambling":
        print("Gambling addiction can severely impact your finances and well-being. Seek out gambling support groups, counseling, and consider self-exclusion programs to limit access to gambling venues.")
    elif d == "shopping":
        print("Shopping addiction can lead to financial stress. Set a budget, track your spending habits, and consider seeking help from a therapist to address underlying issues.")
    elif d == "overeating":
        print("Overeating can often be a way to cope with stress. Focus on mindful eating, create a balanced meal plan, and seek support from a nutritionist or therapist if needed.")
    elif d == "food addiction":
        print("Food addiction can be challenging to manage. Focus on building a healthy relationship with food, consider consulting a nutritionist or therapist, and engage in mindful eating practices.")
    elif d == "pornography" or d=="porn" or d=="Porn":
        print("Pornography addiction can impact relationships and self-esteem. Seek professional therapy, limit access to triggers, and consider joining a support group.")
    elif d == "sex addiction":
        print("Sex addiction can affect your personal life and relationships. Seek professional counseling, join a support group, and work on developing healthy relationship habits.")
    elif d == "workaholism":
        print("Workaholism can lead to burnout and neglect of personal life. Set boundaries for work hours, prioritize self-care, and focus on maintaining a work-life balance.")
    else:
        print("Sorry, I don't have advice for that. Please consult a professional.")

# Call the function initially
give_advice(d)

# Check-up every 2 hours
while True:
    time.sleep(7200)  # Pauses for 2 hours (7200 seconds)
    print("\n2-hour check-in:")
    response = input("How are you feeling now? Do you need advice on anything else? ").lower()
    
    if response != "no":
        give_advice(response)
    else:
        print("Okay, stay strong and take care!")
