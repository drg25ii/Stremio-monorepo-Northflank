FROM registry.hf.space/epcdrg2-torrenthan:latest
USER root
ENV PORT=7860
EXPOSE 7860
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 7002"]
