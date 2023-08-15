# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container to /model
WORKDIR /model

# Add the requirements file to the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /model
COPY selected_any_positive_model.joblib .
COPY selected_Biopsy_model.joblib .
COPY selected_Hinselmann_model.joblib .
COPY selected_Schiller_model.joblib .
COPY api.py .
COPY model.py .

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the application when the container launches
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
