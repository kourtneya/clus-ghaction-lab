FROM python:3.12-alpine

ENV USERNAME=mkuser
ENV USER_ID=4444

WORKDIR /home/

RUN apk add git build-base weasyprint
RUN pip3 install mkdocs mkdocs-material mkdocs-with-pdf Pygments mkdocs-glightbox
RUN pip3 install git+https://github.com/vincentbernat/pygments-ios@d6b79303cd9dda7b7130e2bb06934a8a22470b11

RUN addgroup -g ${USER_ID} ${USERNAME} && \
    adduser -u ${USER_ID} -G ${USERNAME} -s /bin/sh -D ${USERNAME}
 
USER mkuser

COPY . /home

EXPOSE 8000

CMD ["mkdocs", "serve"]