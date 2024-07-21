# Pull official base image
FROM node:22-alpine

# Set working directory
WORKDIR /app

# Install dependencies
COPY package.json ./
COPY package-lock.json ./
RUN npm install

# Copy project
COPY . ./

# Build the app
# RUN cd frontend/web-front
# RUN npm run build
# RUN cd ../../

# Expose port
EXPOSE 3001

# Start the app
CMD ["npm", "start"]