# --------------------------------------------------
# Build the Angular frontend application from source
# --------------------------------------------------
FROM node:20.5-alpine AS node-build-stage

WORKDIR /app

COPY ui/package.json ui/package-lock.json ./

RUN apk update && apk add openjdk17-jre && npm install @openapitools/openapi-generator-cli && npm install
COPY . .
RUN cd ui/ && npm run build

# --------------------------------------------
# Build the python backend application from source
# --------------------------------------------
FROM python:3.11-alpine AS build-release-stage

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY backend/flask/requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY /build/entrypoint.sh /usr/src/app/entrypoint.sh
COPY backend/flask/AiPromptComposerApi/ /usr/src/app/AiPromptComposerApi/
COPY --from=node-build-stage /app/ui/dist/ai-prompt-composer/ /usr/src/app/www

EXPOSE 8080

ENV IS_DOCKER_DEPLOY=True
ENV WEB_BASE_URL=""
ENV OPEN_AI_API_KEY=OPEN_AI_API_KEY
ENV OPEN_AI_API_BASE=OPEN_AI_API_BASE

ENTRYPOINT ["/bin/sh"]

CMD ["entrypoint.sh"]