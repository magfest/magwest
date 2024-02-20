FROM ghcr.io/magfest/ubersystem:main

# install plugins
COPY . plugins/magwest/

RUN /app/env/bin/paver install_deps
