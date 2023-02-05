FROM ghcr.io/magfest/ubersystem:west2022

# install plugins
COPY . plugins/magwest/
RUN git clone --depth 1 --branch west2022 https://github.com/magfest/covid.git plugins/covid

RUN /app/env/bin/paver install_deps
