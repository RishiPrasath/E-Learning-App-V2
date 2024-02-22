import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

# Define your content
content = [
    ("Creating Password-Secured Accounts:", [
        "- Utilize Django's authentication system for account creation and login.",
        "- Store passwords as hash values using secure algorithms like PBKDF2 with SHA256.",
        "- Extend the Django User model for additional information as needed.",
    ]),
    ("Distinct User Types (Students and Teachers):", [
        "- Implement groups and permissions in Django for different user roles.",
        "- Assign specific capabilities and access levels to students and teachers.",
        "- Design distinct functionalities for each user type, like course creation for teachers and course enrollment for students.",
    ]),
    ("Collecting and Storing User Information:", [
        "- Gather essential details such as username, email, real name, and photo.",
        "- Include additional fields for teachers like bio/qualifications.",
        "- Ensure privacy and data protection in line with relevant laws.",
    ]),
    ("Entities and Relationships Consideration:", [
        "- Plan an overview of entities like users, courses, enrollments, feedback, and materials.",
        "- Focus on the relationships and interactions between these entities for detailed future discussion.",
    ]),
    ("User Home Page Features:", [
        "- Display user information prominently, including username, real name, and photo.",
        "- Show registered courses, upcoming deadlines, and status updates dynamically.",
        "- Plan for home page discoverability and visibility with appropriate privacy controls.",
    ]),
    ("Students Posting Status Updates on Home Page:", [
        "- Enable students to post status updates on their home pages.",
        "- Include features for text input, multimedia attachments, and real-time visibility.",
        "- Consider privacy and visibility settings for these updates.",
    ]),
    ("Course Feedback by Students (Finalized Discussion Point):", [
        "- Implement a feedback mechanism for students to leave ratings and reviews on courses.",
        "- Design an intuitive feedback form within the course interface, accessible at appropriate times.",
        "- Establish a CourseFeedback table, relating it to Student and Course tables to store feedback.",
        "- Map relationships to allow for a one-to-many link between Course and Course_Feedback, and a many-to-many link between Student and Course.",
        "- Use feedback data for continuous course improvement and to inform student course selection.",
    ]),
    ("Search Functionality for Teachers (Finalized Discussion Point):", [
        "- Equip teachers with the ability to search for students and other teachers within the platform.",
        "- Optimize search with indexes and leverage Django’s Q objects for advanced queries.",
        "- Set boundaries on searchable student information for privacy compliance.",
        "- Implement intuitive UI for search, with considerations for student search limitations and privacy.",
        "- Design the search functionality to ensure a balance between user discoverability and data protection.",
    ]),
    ("Course Creation and Material Upload by Teachers (Finalized):", [
        "- Enable teachers to create courses and upload materials.",
        "- Implement file upload functionality and organize files by course and user role.",
        "- Plan for dynamic directory structures and efficient file retrieval.",
        "- Address version control for course materials to manage updates.",
    ]),
    ("Course Management and Student Enrollment Visibility for Teachers (Finalized):", [
        "- Develop features for teachers to view their courses and see lists of enrolled students.",
        "- Define course fields and manage the many-to-many relationship between students and courses.",
        "- Provide functionalities for real-time enrollment updates and enrollment management.",
    ]),
    ("Real-Time Communication with Web Sockets (Finalized):", [
        "- Establish real-time communication channels using WebSockets for features like text chat.",
        "- Utilize Django Channels to manage WebSocket connections and messages.",
        "- Implement consumers for WebSocket session management.",
        "- Secure WebSocket connections with appropriate authentication.",
        "- Design the client-side to handle real-time UI updates and user notifications.",
        "- Ensure scalability and robustness through testing and using a channel layer like Redis.",
    ]),
    ("Comprehensive Requirements for eLearning Platform (Finalized):", [
        "- Account creation and management functions with secure login and logout processes.",
        "- Teachers' ability to search for students and others, add new courses, and remove/block students.",
        "- Students' ability to enroll in courses, leave feedback, and chat in real-time.",
        "- Both students and teachers can post status updates, with teachers additionally able to upload course files.",
        "- Notifications for user actions such as course enrollments and material additions.",
        "- Technical requirements for the proper use of Django models, migrations, forms, validators, serialization, Django REST framework, URL routing, and unit testing.",
        "- A robust database model to effectively handle the relationships between accounts, courses, and user interactions.",
        "- Implementation of a RESTful interface for user data access and server-side code testing.",
    ])
]

# Get the current directory
current_directory = os.getcwd()

# Create a PDF document in the current directory
pdf_file_path = os.path.join(current_directory, "eLearning_App_Requirements.pdf")
doc = SimpleDocTemplate(pdf_file_path, pagesize=letter)

# Create a list of paragraphs with specified styles
styles = getSampleStyleSheet()
elements = []

for heading, points in content:
    elements.append(Paragraph(heading, styles['Heading1']))

    # Create a table for bullet points
    bullet_points = [(f"{i+1}.", point) for i, point in enumerate(points)]
    table = Table(bullet_points, colWidths=[20, 400])
    table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONT_SIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
    ]))
    elements.append(table)

# Build the PDF document
doc.build(elements)

print(f"PDF file created at: {pdf_file_path}")
