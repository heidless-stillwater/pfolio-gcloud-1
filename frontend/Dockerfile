FROM node:17.3-alpine
WORKDIR /frontend
COPY package.json .
RUN npm install
COPY . .
RUN npm run build
COPY . .
CMD ["npm", "start"]