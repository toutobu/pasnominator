FROM python:3.7-alpine
WORKDIR /app

ENV MECAB_VERSION=0.996
ENV MECAB_URL='https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7cENtOXlicTFaRUE'
ENV MECAB_IPADIC_VERSION=2.7.0-20070801
ENV MECAB_IPADIC_URL='https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7MWVlSDBCSXZMTXM'

RUN apk add --no-cache make gcc g++ swig \
# mecab
  && cd /opt \
  && wget -O mecab-${MECAB_VERSION}.tar.gz $MECAB_URL \
  && tar zxvf mecab-${MECAB_VERSION}.tar.gz \
  && cd mecab-${MECAB_VERSION} \
  && ./configure \
  && make \
  && make install \
# mecab ipadic
  && cd /opt \
  && wget -O mecab-ipadic-${MECAB_IPADIC_VERSION}.tar.gz $MECAB_IPADIC_URL \
  && tar zxvf mecab-ipadic-${MECAB_IPADIC_VERSION}.tar.gz \
  && cd mecab-ipadic-${MECAB_IPADIC_VERSION} \
  && ./configure  --with-charset=utf8 \
  && make \
  && make install \
# cleanup
  && cd /opt \
  && rm -rf \
     mecab-${MECAB_VERSION}.tar.gz \
     mecab-${MECAB_VERSION} \
     mecab-ipadic-${MECAB_IPADIC_VERSION}.tar.gz zxvf \
     mecab-ipadic-${MECAB_IPADIC_VERSION}

ADD pyproject.toml /app/pyproject.toml

RUN apk add --no-cache \
  build-base \
  libffi-dev \
  openssl-dev \
  && pip install poetry \
  && poetry install

ADD . /app
