FROM deepset/hayhooks:main

COPY requirements.txt requirements.txt 
ARG src="comments-2024-09-07 22:44:00.473900.csv"
COPY ${src} ${src}
RUN pip install -r requirements.txt