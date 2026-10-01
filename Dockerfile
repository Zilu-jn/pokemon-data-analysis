# Repository A - W4: Containerize the Pokémon analysis
FROM python:3.12-slim

# Store the project inside /app in the container
WORKDIR /app

# Install project dependencies
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

# Copy only the files needed to run the analysis
COPY analysis.py pokemon_pipeline.py ./
COPY data ./data

# Create the folder used for the chart
RUN mkdir -p images

# Allow Matplotlib to work without opening a window
ENV MPLBACKEND=Agg
ENV PYTHONUNBUFFERED=1

# Run the analysis when the container starts
CMD ["python", "analysis.py"]