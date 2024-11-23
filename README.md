# WebApp

DOCX to PDF Converter Web Application
This web application allows users to upload .docx files, converts them to PDF, displays metadata of the uploaded file, and provides the option to download the converted PDF. This application is designed using Flask, Docker, and Kubernetes.

Features
Upload .docx File: Allows users to upload .docx files.
File Conversion: Converts uploaded .docx files to PDF format.
File Metadata: Displays file metadata such as filename, size, and last modified date.
Download PDF: Users can download the converted PDF file.
UI Interface: Simple frontend to interact with the web application.
Dockerized: The application is Dockerized for easy deployment.
Kubernetes Support: Kubernetes manifests to deploy the application in a cluster.
Technologies Used
Backend: Flask
Frontend: HTML, CSS, JavaScript
PDF Conversion: fpdf, python-docx
Containerization: Docker
Container Orchestration: Kubernetes
CI/CD: GitHub Actions
Project Structure
php
Copy code
docx-to-pdf-webapp/
├── app.py                # Flask application code
├── Dockerfile            # Dockerfile for containerizing the app
├── requirements.txt      # Python dependencies
├── k8s/                  # Kubernetes deployment files
│   ├── deployment.yaml   # Kubernetes deployment
│   ├── service.yaml      # Kubernetes service
├── scripts/              # Helper scripts (e.g., bash scripts)
│   ├── run.sh            # Script to build and run Docker container
└── templates/            # HTML templates
    ├── index.html        # Main user interface
└── static/               # Static files
    └── styles.css        # Basic styling for the frontend
Installation Instructions
1. Clone the repository
bash
Copy code
git clone https://github.com/your-username/docx-to-pdf-webapp.git
cd docx-to-pdf-webapp
2. Install dependencies
To install the required dependencies for Flask:

bash
Copy code
pip install -r requirements.txt
3. Running the application locally
You can run the Flask app locally with the following command:
bash
Copy code
python app.py
Visit http://localhost:5000 in your browser to interact with the app.
4. Running with Docker
Build and run the Docker container:
bash
Copy code
./scripts/run.sh
The app will be available at http://localhost:5000.
5. Deploying to Kubernetes
Apply the Kubernetes configurations:
bash
Copy code
kubectl apply -f k8s/
Expose the service using kubectl expose or use a LoadBalancer service to access the app externally.
6. CI/CD Pipeline
The project includes a GitHub Actions pipeline to automatically build and push the Docker image to DockerHub upon pushing changes to the main branch.
How to Use
Upload DOCX File: Use the file input to upload a .docx file.
Conversion: Once uploaded, the app will process the file and convert it to a PDF.
View Metadata: Metadata such as file name, size, and last modification date will be shown.
Download PDF: A link will be provided to download the converted PDF file.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Methodology
The development of this DOCX to PDF converter follows a structured methodology to ensure that the system is robust, efficient, and easy to deploy. Below is the methodology used in this project:

1. Requirement Analysis
User Needs: The system must enable users to upload .docx files, convert them to PDFs, view file metadata, and download the converted PDFs.
Key Features: File upload, file conversion, metadata display, and PDF download.
Non-Functional Requirements: The system should be reliable, easy to use, and scalable.
2. System Design
Backend:
Flask Framework: Chosen for its simplicity and lightweight nature, Flask provides an easy way to set up a REST API for file uploading, conversion, and downloading.
PDF Conversion: The conversion of .docx files to PDFs is done using Python libraries like python-docx (to read .docx files) and fpdf (to create PDFs).
File Metadata: File metadata such as size, name, and last modification time is obtained using Python’s os library.
Frontend:
A simple HTML/CSS/JavaScript interface is provided to allow users to upload files and view the results.
JavaScript handles form submission and the dynamic display of results (like metadata and download links).
Containerization:
Docker: The application is Dockerized to ensure consistency across environments and to make it easy to deploy on any system.
A Dockerfile is created to define the dependencies and setup steps for the container.
Orchestration:
Kubernetes: Kubernetes is used to provide scalability and orchestration, making it easy to deploy the application in production environments.
A Kubernetes deployment and service are created to handle container deployment and load balancing.
3. Development Phases
Phase 1: Prototyping and Design
A basic Flask app was created to handle file uploads and conversion.
The initial UI was created to support file uploads and display the results.
Phase 2: Conversion Logic
The core functionality of converting .docx files to PDFs was developed. This includes reading the .docx content using python-docx and converting the text into PDF format using fpdf.
Phase 3: File Metadata Extraction
Metadata such as file name, size, and last modified date was extracted using Python’s os library.
Phase 4: Frontend Development
The frontend was built with HTML and CSS to ensure that users could easily interact with the application.
JavaScript was used to handle the file upload and display results dynamically.
Phase 5: Dockerization
The app was Dockerized by creating a Dockerfile to containerize the application and a shell script (run.sh) to build and run the container.
Phase 6: Kubernetes Deployment
Kubernetes configurations (deployment.yaml and service.yaml) were created to deploy the app on a Kubernetes cluster, ensuring scalability.
4. Testing
Testing was conducted to ensure:

File Upload: Verifying that the application correctly uploads .docx files.
Conversion Accuracy: Testing the accuracy of the DOCX to PDF conversion.
File Metadata: Ensuring that the correct metadata is displayed.
Container and Orchestration: Testing the Docker container and Kubernetes deployment to ensure the app can be run in various environments.
5. Deployment and CI/CD
The application was deployed using:

GitHub Actions: A CI/CD pipeline was set up using GitHub Actions to automatically build and push Docker images to DockerHub.
Docker: The app was run locally and in Docker containers for consistency.
Kubernetes: The app was deployed on Kubernetes to handle scaling and orchestration.
6. Future Enhancements
Password Protection for PDFs: A feature to add password protection to PDFs.
Microservices Architecture: Further breakdown of the app into separate microservices (e.g., one for file conversion, another for metadata extraction, etc.).
User Authentication: Adding user login and account management features.
