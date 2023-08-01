FROM ghcr.io/magfest/ubersystem:west2023

# install plugins
COPY . plugins/magwest/
RUN git clone --depth 1 --branch west2023 https://github.com/magfest/covid.git plugins/covid

RUN /app/env/bin/paver install_deps
