FROM ghcr.io/magfest/ubersystem:west2022

# add our code
COPY . plugins/magwest/
RUN if [ -d plugins/magwest/plugins ]; then mv plugins/magwest/plugins/* plugins/; fi
RUN /app/env/bin/paver install_deps
