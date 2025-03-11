# Specify the base image from the node official images
FROM node:18

# Install PNPM
RUN npm install -g pnpm

# Create a non-root user and switch to it
RUN adduser --disabled-password --gecos '' appuser
USER appuser

# Create app directory inside the image
WORKDIR /app

# Copy package files and install dependencies
COPY --chown=appuser:appuser package.json pnpm-lock.yaml ./
RUN pnpm install

# Copy the source files and give proper permissions
COPY --chown=appuser:appuser . .

# If you need to build your Nuxt app for production, uncomment the following line
# RUN pnpm run build

# Expose the port the app runs on
EXPOSE 3000

# Define the command to run your app
CMD ["pnpm", "run", "dev"]
