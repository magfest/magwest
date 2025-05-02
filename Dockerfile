FROM ghcr.io/magfest/ubersystem:weststock2025
ENV uber_plugins=["magwest"]

# install plugins
COPY . plugins/magwest/

RUN $HOME/.local/bin/uv pip install --system -r requirements.txt;
