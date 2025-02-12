FROM node:18-alpine
 
WORKDIR /app
 
COPY package*.json ./
 
RUN npm install
 
COPY . .
 
EXPOSE 3000

RUN npm install --save-dev web-vitals
 
CMD ["npm", "start"]