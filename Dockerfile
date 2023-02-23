FROM ghcr.io/magfest/ubersystem:west2020

# install plugins
COPY . plugins/magwest/

RUN /app/env/bin/paver install_deps
