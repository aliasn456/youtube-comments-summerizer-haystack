FROM deepset/hayhooks:main

COPY requirements.txt requirements.txt 
ARG src="comments-2024-08-31 22:51:22.924448.csv"
COPY ${src} ${src}
RUN pip install -r requirements.txt