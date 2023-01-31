FROM ghcr.io/magfest/covid:west2022

# add our code
COPY . plugins/magwest/
RUN if [ -d plugins/magwest/plugins ]; then echo "copying plugins"; ls plugins/magwest/plugins/*; mv plugins/magwest/plugins/* plugins/; fi
RUN /app/env/bin/paver install_deps
