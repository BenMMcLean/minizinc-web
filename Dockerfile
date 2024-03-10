FROM minizinc/minizinc:2.5.5

ENV PYTHONUNBUFFERED=1

# Install Python3.8 and some packages
RUN apt update \
    && DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt install -yqq pkg-config wget git gnupg curl python3.8 python3-pip libmysqlclient-dev
RUN pip3 install pipenv
RUN pip3 install gunicorn

# Copy source files
COPY . /app
WORKDIR /app
RUN pipenv install --system --deploy --ignore-pipfile

# Expose web server port & execute
EXPOSE 5000
CMD ["python", "main.py"]