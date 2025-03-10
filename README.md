# Inter IIT Tech Meet 13.0: Chandrayaan Moon Mapping Challenge 

## Overview

This repository contains our solution to the Moon Mapping problem statement presented at the Inter IIT Tech Meet 13.0. The challenge, sponsored by ISRO, required participants to develop innovative solutions within the field of astronomy. ([interiit-tech.com](https://interiit-tech.com/problem-statement/?utm_source=chatgpt.com))

## Problem Statement

The specific problem statement, released by ISRO for the high-prep category, tasked teams with addressing a complex issue in astronomy. Detailed information about the problem can be found on the official Inter IIT Tech Meet website. ([interiit-tech.com](https://interiit-tech.com/problem-statement/?utm_source=chatgpt.com))

## Solution Approach

Our approach to solving this problem involved the following key steps:

1. **Problem Analysis**: We thoroughly analyzed the problem statement to understand the requirements and constraints.
2. **Literature Review**: Conducted an extensive review of existing methodologies and technologies relevant to the problem.
3. **Design and Development**: Developed a solution leveraging advanced algorithms and technologies pertinent to astronomy.
4. **Testing and Validation**: Rigorously tested our solution against various scenarios to ensure accuracy and reliability.

## Repository Structure

The repository is organized as follows:

- `Inter_iit_isro-main/`: Contains the main implementation of our solution, including source code and related resources.
- `Mapping_isro/`: Includes mapping data and scripts utilized in our solution.
- `.gitignore`: Specifies files and directories to be ignored by Git.

## Dependencies

Our project utilizes the following technologies:

- **Python**: The core programming language used for development.
- **TypeScript**: Employed for certain components requiring robust type definitions.
- **C, C++, Fortran**: Used in performance-critical sections of the code.
- **Cython**: Facilitated the integration of C/C++ code with Python.

## Getting Started

To set up the project locally, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/sujalk777/Inter_IIT_13.0.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd Inter_IIT_13.0
   ```

3. **Install Dependencies**:

   Ensure you have Python 3.10 installed. Then, install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:

   Create a `.env` file in the main folder with the following content:

   ```
   GMAPS_API_KEY=your_key
   DWAVE_TOKEN=your_token
   flight_mail=your_mail
   flight_mail_password=your_password
   ```

   - `GMAPS_API_KEY`: Obtain from the Google Distance Matrix API.
   - `DWAVE_TOKEN`: Acquire from D-Wave's official website.
   - `flight_mail` and `flight_mail_password`: Credentials for the email service used in the project.

## Usage

After setting up the environment, you can run the main application using:

```bash
python main.py
```

Replace `main.py` with the actual entry point of the application.

