# Use Miniforge3 (conda-forge) as base image
FROM condaforge/miniforge3:latest

# Set the working directory inside the container to /app
WORKDIR /app

# Copy environment.yml file from the host into the container
COPY environment.yml .

# Create conda environment named "fin-dash" and clean caches
RUN conda env create -f environment.yml && conda clean -afy

# Ensure subsequent commands run in the "fin-dash" conda environment
SHELL ["conda", "run", "-n", "fin-dash", "/bin/bash", "-c"]

# Copy the entire project directory into the container
COPY . .

EXPOSE 8050

# Define the default command to run when the container starts
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "fin-dash", "gunicorn", "wsgi:server", "-b", "0.0.0.0:8050", "-w", "4"]
