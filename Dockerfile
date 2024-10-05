FROM ghcr.io/magfest/ubersystem:west2024
ENV uber_plugins=["magwest"]

# install plugins
COPY . plugins/magwest/

RUN uv pip install --system -r plugins/magwest/requirements.txt
