FROM registry.hf.space/epcdrg2-torrenthan:latest
USER root
ENV PORT=7002
EXPOSE 7002
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 7002"]
