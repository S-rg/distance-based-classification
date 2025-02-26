FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir numpy pandas scikit-learn wandb
EXPOSE 8888
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
