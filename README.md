# WebApp


## **Methodology**

The development of the DOCX to PDF converter web application follows a systematic and structured methodology to ensure the system meets the desired functional and non-functional requirements. The methodology can be broken down into the following phases:

### **1. Requirement Analysis**

The primary objective of the project is to create a web application that allows users to upload `.docx` files, converts them to PDF format, and provides an option to download the converted PDF. Additionally, the system should display metadata such as file name, size, and last modified date of the uploaded file. The requirements were identified as follows:

- **Functional Requirements**:
  - Users should be able to upload `.docx` files.
  - The system should convert the uploaded `.docx` files into PDFs.
  - The system should display metadata of the uploaded files.
  - Users should be able to download the converted PDF files.

- **Non-Functional Requirements**:
  - The system should be reliable, easy to use, and scalable.
  - The application should be containerized and easily deployable in different environments.

### **2. System Design**

#### **Backend Design**:
- **Flask Framework**: Flask was chosen for its simplicity and flexibility. It provides a lightweight environment to handle file uploads, PDF conversion, and metadata extraction.
- **File Conversion Logic**: The core conversion functionality involves reading `.docx` files using the `python-docx` library and converting them into PDFs using the `fpdf` library.
- **Metadata Extraction**: Metadata such as file name, size, and last modified time is retrieved using Python’s `os` library.

#### **Frontend Design**:
- **HTML, CSS, and JavaScript**: A simple and user-friendly interface was developed to allow users to upload `.docx` files, view conversion results, and download the converted PDFs. JavaScript was used to dynamically display the results and handle form submissions without page reloads.

#### **Containerization**:
- **Docker**: Docker was used to containerize the application. This ensures that the app runs consistently across different environments and simplifies the deployment process.
- The Dockerfile specifies the environment setup, including dependencies and the runtime configuration.

#### **Orchestration**:
- **Kubernetes**: Kubernetes manifests were created to deploy and manage the application in a cloud environment. Kubernetes allows for easy scaling and management of the app’s containers, making it suitable for production-grade deployments.

### **3. Development Phases**

#### **Phase 1: Prototyping and Design**
- The initial prototype was developed using Flask to handle basic file upload functionality and display the result. This phase focused on ensuring the core features like file upload and PDF conversion were functional.

#### **Phase 2: Core Functionality**
- The file conversion process was implemented using `python-docx` for reading `.docx` files and `fpdf` for generating PDF files. The file metadata (e.g., file size and last modified date) was extracted and displayed in the UI.

#### **Phase 3: Frontend Development**
- A user-friendly HTML form was designed to allow users to upload `.docx` files. The frontend also includes basic styling for an intuitive experience.
- JavaScript was used to handle asynchronous form submissions and display the PDF download link and metadata dynamically without refreshing the page.

#### **Phase 4: Dockerization**
- The Flask app was containerized using Docker. A Dockerfile was created to specify the necessary dependencies and environment setup for the application.
- A shell script (`run.sh`) was developed to streamline the build and deployment process of the Docker container.

#### **Phase 5: Kubernetes Deployment**
- Kubernetes deployment and service files were created to facilitate scaling and easy deployment. These files enable the app to run in a Kubernetes cluster and can be easily managed and scaled as required.
  
#### **Phase 6: CI/CD Implementation**
- A GitHub Actions pipeline was set up to automatically build and push the Docker image to DockerHub whenever changes are pushed to the repository. This ensures continuous integration and delivery, making the process more efficient.

### **4. Testing**

- **Functional Testing**: Testing was conducted to ensure that the file upload functionality works as expected, and the DOCX to PDF conversion is accurate.
- **UI Testing**: The frontend was tested to ensure that the file upload form works seamlessly and displays metadata and PDF download links correctly.
- **Container and Deployment Testing**: The Docker container was tested to ensure consistency across different environments, and the Kubernetes deployment was verified to ensure the app scales and functions correctly in a cloud environment.

### **5. Deployment**

- The application was deployed on a local machine for testing purposes using Docker. For production environments, Kubernetes was used to deploy the app in a scalable and manageable way.
- The CI/CD pipeline ensures that the Docker image is automatically built and pushed to DockerHub, making the deployment process streamlined and automated.

