FROM ghcr.io/magfest/ubersystem:main
ENV uber_plugins=["magwest"]

# install plugins
COPY . plugins/magwest/

RUN /root/.local/bin/uv pip install --system -r requirements.txt;