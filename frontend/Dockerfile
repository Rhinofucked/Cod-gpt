FROM arm32v7/node:20-alpine
WORKDIR /app
COPY . .
RUN npm install && npm run build
CMD ["npm", "run", "dev"]