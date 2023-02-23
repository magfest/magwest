FROM ghcr.io/magfest/ubersystem:west2019

# install plugins
COPY . plugins/magwest/

RUN /app/env/bin/paver install_deps
