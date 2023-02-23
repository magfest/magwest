FROM ghcr.io/magfest/ubersystem:west2021

# install plugins
COPY . plugins/magwest/
RUN git clone --depth 1 --branch west2021

RUN /app/env/bin/paver install_deps