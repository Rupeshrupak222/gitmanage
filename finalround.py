import streamlit as st
import os
import cv2
import base64
import numpy as np
import smtplib
import geocoder
import requests
import pandas as pd
import psutil
import paramiko
import boto3
from email.message import EmailMessage
from twilio.rest import Client
from sklearn.linear_model import LinearRegression
from pymongo import MongoClient

# ----- Configuration ----- #
EMAIL_ADDRESS = "your_email@example.com"
EMAIL_PASSWORD = "your_password"
TWILIO_SID = "your_twilio_sid"
TWILIO_AUTH = "your_twilio_auth_token"
TWILIO_PHONE = "+1234567890"
RECIPIENT_PHONE = "+1987654321"
AWS_ACCESS_KEY = "your_aws_access_key"
AWS_SECRET_KEY = "your_aws_secret_key"

st.set_page_config(layout="wide")
st.title("📋 Summer internship Task")
st.markdown("### 👨‍💻 Rupesh Kumar Rupak - Team 29")
st.markdown("[🔗 GitHub](https://github.com/Rupeshrupak222) | [🔗 LinkedIn](https://www.linkedin.com/in/rupesh-kumar-rupak-bb4b44265/) | [🚀 ShareGo Startup](https://sharego1.netlify.app/)")

main_menu = st.sidebar.selectbox("Select a Section", [
    "Python Tasks", "Linux", "DevOps", "Full Stack", "Machine Learning", "AWS", "Projects"])

# ----- Python Tasks ----- #
if main_menu == "Python Tasks":
    menu = st.selectbox("Select a Task", [
        "Face Swap", "Compare LLaMA vs DeepSeek", "RAM Usage", "Create Digital Image",
        "List vs Tuple", "Google Search", "Send Anonymous Email",
        "Post to Social Media", "Send LinkedIn Message"])

    if menu == "Face Swap":
        st.header("🔄 Face Swap (Demo Mode)")
        st.warning("Feature available in offline version using OpenCV and dlib.")

    elif menu == "Compare LLaMA vs DeepSeek":
        st.header("🧠 LLaMA vs DeepSeek LLM Comparison")
        st.markdown("""
        - **LLaMA**: Meta's model with strong topic understanding and efficiency.
        - **DeepSeek**: Alibaba's multilingual and domain-specific focus.
        """)

    elif menu == "RAM Usage":
        st.header("💾 RAM Usage")
        mem = psutil.virtual_memory()
        st.write(f"Total: {mem.total // (1024**2)} MB")
        st.write(f"Available: {mem.available // (1024**2)} MB")
        st.write(f"Used: {mem.used // (1024**2)} MB")
        st.write(f"Percent: {mem.percent}%")

    elif menu == "Create Digital Image":
        st.header("🖼️ Create Digital Image")
        img = np.zeros((200, 400, 3), dtype=np.uint8)
        img[:] = (255, 0, 0)
        cv2.putText(img, "Hello", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)
        st.image(img, channels="BGR")

    elif menu == "List vs Tuple":
        st.header("📚 List vs Tuple - Python")
        st.markdown("""
        | Feature        | List           | Tuple          |
        |----------------|----------------|----------------|
        | Mutable        | ✅ Yes         | ❌ No          |
        | Syntax         | `[]`           | `()`           |
        | Performance    | Slower         | Faster         |
        | Use Case       | Dynamic data   | Fixed data     |
        """)

    elif menu == "Google Search":
        st.header("🔍 Google Search (Browser-based)")
        query = st.text_input("Enter your search query")
        if st.button("Search"):
            search_url = f"https://www.google.com/search?q={requests.utils.quote(query)}"
            st.markdown(f"[Click to Search on Google]({search_url})", unsafe_allow_html=True)

    elif menu == "Send Anonymous Email":
        st.header("📧 Send Anonymous Email (Simulated)")
        fake_sender = st.text_input("From (Fake Email)")
        to = st.text_input("To")
        sub = st.text_input("Subject")
        body = st.text_area("Body")
        if st.button("Send Anonymously"):
            st.warning("This is a simulated function.")
            st.success(f"Email sent from {fake_sender} to {to} (simulated)")

    elif menu == "Post to Social Media":
        st.header("📤 Post to Social Media")
        msg = st.text_area("Write your post")
        platform = st.selectbox("Select platform", ["Twitter/X", "Instagram", "Facebook"])
        if st.button("Post"):
            st.success(f"Posted to {platform} (simulated): {msg}")

    elif menu == "Send LinkedIn Message":
        st.header("💼 Send LinkedIn Message")
        name = st.text_input("Recipient Name")
        message = st.text_area("Message")
        if st.button("Send Message"):
            st.success(f"LinkedIn message to {name} sent (simulated).")

# ----- Linux Section ----- #
elif main_menu == "Linux":
    st.header("🐧 Linux SSH Command Executor")
    host = st.text_input("Enter SSH IP/Hostname")
    user = st.text_input("Enter SSH Username")
    password = st.text_input("Enter SSH Password", type="password")
    command = st.text_area("Enter Linux Command to Execute")
    if st.button("Execute over SSH"):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=host, username=user, password=password)
            stdin, stdout, stderr = client.exec_command(command)
            st.code(stdout.read().decode())
            st.error(stderr.read().decode())
            client.close()
        except Exception as e:
            st.error(f"SSH Connection Failed: {e}")

# ----- DevOps Section ----- #
elif main_menu == "DevOps":
    st.header("⚙️ DevOps Task Runner")
    task = st.selectbox("Choose DevOps Task", ["Check Docker Status", "List Docker Containers", "Check System Services", "Show Disk Usage"])
    host = st.text_input("SSH IP")
    user = st.text_input("Username")
    password = st.text_input("Password", type="password")
    task_cmds = {
        "Check Docker Status": "systemctl status docker",
        "List Docker Containers": "docker ps -a",
        "Check System Services": "systemctl list-units --type=service --state=running",
        "Show Disk Usage": "df -h"
    }
    if st.button("Run DevOps Task"):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=host, username=user, password=password)
            stdin, stdout, stderr = client.exec_command(task_cmds[task])
            st.code(stdout.read().decode())
            st.error(stderr.read().decode())
            client.close()
        except Exception as e:
            st.error(f"SSH Connection Failed: {e}")

# ----- Full Stack Section ----- #
elif main_menu == "Full Stack":
    st.header("🌐 Full Stack Task Runner")
    fs_task = st.selectbox("Choose Full Stack Task", ["Start React Dev Server", "Build React Project", "Start Node.js Backend", "Check NGINX Config"])
    host = st.text_input("SSH IP")
    user = st.text_input("Username")
    password = st.text_input("Password", type="password")
    fs_cmds = {
        "Start React Dev Server": "cd myapp && npm start",
        "Build React Project": "cd myapp && npm run build",
        "Start Node.js Backend": "cd backend && node index.js",
        "Check NGINX Config": "nginx -t"
    }
    if st.button("Run Full Stack Task"):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=host, username=user, password=password)
            stdin, stdout, stderr = client.exec_command(fs_cmds[fs_task])
            st.code(stdout.read().decode())
            st.error(stderr.read().decode())
            client.close()
        except Exception as e:
            st.error(f"SSH Connection Failed: {e}")

# ----- ML Section ----- #
elif main_menu == "Machine Learning":
    st.header("🤖 Linear Regression - Predict House Price")
    ml_file = st.file_uploader("Upload CSV (Size, Price)", type="csv")
    if ml_file is not None:
        data = pd.read_csv(ml_file)
        st.write(data.head())
        X = data[['Size']]
        y = data['Price']
        model = LinearRegression()
        model.fit(X, y)
        input_size = st.number_input("Enter House Size (sqft)", min_value=100)
        if st.button("Predict Price"):
            pred = model.predict([[input_size]])[0]
            st.success(f"Predicted Price: ${pred:,.2f}")

# ----- AWS Section ----- #
elif main_menu == "AWS":
    st.header("☁️ AWS Task Runner")
    service = st.selectbox("Choose AWS Service", ["List EC2 Instances", "List S3 Buckets"])
    if st.button("Run AWS Task"):
        try:
            session = boto3.Session(
                aws_access_key_id=AWS_ACCESS_KEY,
                aws_secret_access_key=AWS_SECRET_KEY,
                region_name="us-east-1"
            )
            if service == "List EC2 Instances":
                ec2 = session.client('ec2')
                instances = ec2.describe_instances()
                st.json(instances)
            elif service == "List S3 Buckets":
                s3 = session.client('s3')
                buckets = s3.list_buckets()
                st.json(buckets)
        except Exception as e:
            st.error(f"AWS Task Failed: {e}")

# ----- Projects Section ----- #
elif main_menu == "Projects":
    st.header("🚀 Project Portfolio")
    projects = [
        "Smart Farming (AI)",
        "Mess Menu Project",
        "Weather Forecasting",
        "Portfolio Project",
        "Chatbot (Genetic AI + LangChain)",
        "Linear Regression",
        "Flask Task App",
        "Android Studio Project",
        "Jenkins CI/CD",
        "ShareGo Startup"
    ]
    for i, project in enumerate(projects, start=1):
        st.subheader(f"Project {i}: {project}")
        st.markdown("""
        - 🔗 [Code](#) | 🔗 [GitHub](#) | 🔗 [Live Demo](#) | 🔗 [LinkedIn](#)
        """)
