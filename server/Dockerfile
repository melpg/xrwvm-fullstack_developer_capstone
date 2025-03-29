#should have the following steps listed:
#Add a base image.
#Add the requirements.txt file.
#Install and update Python.
#Change the working directory.
#Expose port.
#Run the command to start the application.
FROM python:3.12.0-slim-bookworm

ENV PYTHONBUFFERED 1
ENV PYTHONWRITEBYTECODE 1

ENV APP=/app

#Change the workdir
WORKDIR $APP

#Install the requirements
COPY requirements.txt $APP

RUN pip install --no-cache-dir -r requirements.txt

#Copy the rest of the files
COPY . $APP/

# Copy static files to the correct location
RUN mkdir -p /app/staticfiles
COPY --from=build-stage /app/frontend/build/static /app/staticfiles/


#Expose the port
EXPOSE 8000

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT [ "/bin/bash", "/app/entrypoint.sh" ]

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangoproj.wsgi"]
