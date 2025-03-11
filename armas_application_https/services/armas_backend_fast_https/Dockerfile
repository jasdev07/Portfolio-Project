# Stage 1: Build the application
FROM condaforge/miniforge3:24.3.0-0 as builder
ARG DEBIAN_FRONTEND=noninteractive

# Set the working directory
WORKDIR /app

# Copy the environment.yml file
COPY environment.yml /app/environment.yml

# Install dependencies
RUN apt update
RUN apt-get install libtiff5-dev libjpeg8-dev libopenjp2-7-dev zlib1g-dev \
libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk \
libharfbuzz-dev libfribidi-dev libxcb1-dev -y

# Create the Conda environment
RUN mamba env create -f /app/environment.yml

# Ensure the environment is activated
ENV PATH /opt/conda/envs/armas/bin:$PATH

# Install the requirements using pip (if any)
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the source code to the container
COPY ./src /app/src

# Obfuscate code
RUN pyarmor gen -O dist -r -i src

# Run any build or compile steps if necessary
# For example: RUN python -m compileall /app/src

# Stage 2: Create the final runtime image
FROM condaforge/miniforge3:24.3.0-0

# Set the working directory
WORKDIR /app

# Copy only the necessary artifacts from the builder stage
COPY --from=builder /opt/conda/envs/armas /opt/conda/envs/armas
COPY --from=builder /app/dist /app/dist
COPY ./models /app/models


# Ensure the environment is activated
WORKDIR /app/dist
ENV PATH /opt/conda/envs/armas/bin:$PATH
ENV PYTHONPATH="${PYTHONPATH}:/app/dist"

# Command to run the application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8085"]
