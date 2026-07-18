---
title: "Regressive JPEGs: (Maurycy's blog)"
url: https://maurycyz.com/projects/bad_jpeg/
date: 2026-07-18
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-07-18T11:32:37.244790
---

# Regressive JPEGs: (Maurycy's blog)

**Regressive JPEG Optimization**

## Overview

This article explores the concept of regressive JPEG optimization, where compressed data is partially unloaded and reloaded in lower resolution to improve image quality.

### Key Takeaways

* Regressive JPEG allows for partial reconstruction of lost low-frequency components.
* Multiple scans are used to reconstruct the image in a segmented manner.
* Concatenation of these images avoids the need for individual scans, but can be slow and inefficient due to network bandwidth limitations.

### Main Points

* Scans are separated by 0-100 bytes and contain:
	+ Compression metadata
	+ Channel id (3-5)
	+ DCT coefficients
	+ Huffman-coded quantization parameters
* Image is concatenated into multiple images, which can be used for progressive rendering.
* Decoding will switch between scanned images as required.

### Example Scenario

When served over a slow network, this concatenated file may:

* Switch between 10-20 scans, depending on decoding hardware and bandwidth.
* Experience decoding delays due to repeated encoding/decoding cycles.

### Limitations and Trade-Offs

* Decoders can only handle up to 9 scans before becoming inefficient or failing to decode accurately.
* Concatenation can be slow and may not provide significant benefits for high-resolution images.

**Code Walkthrough (C Program)**

To demonstrate regressive JPEG optimization in a quick and dirty manner, the author used a C program to concatenate multiple images. Here's the code:
```c
#include <stdio.h>

#define MAX_ITER 9

// Function to load compressed data from image file
size_t readCompressed(const char *imageFile, unsigned char **compressedData) {
    // Implementation omitted for brevity
}

int main() {
    unsigned char *huffmanCodedDCTCoefficients = NULL;
    int len = readCompressed("image.bin", &huffmanCodedDCTCoefficients);
    
    for (int i = 0; i < MAX_ITER; i++) {
        // Concatenate images by re-reading and re-compressing data
        unsigned char *tempData = malloc(len + 4 * MAX_ITER); // Assume max len:1022 bytes/scan * MAX_ITER scans
        unsigned char *newCompressedData = NULL;
                
        for (int s = 0; s < MAX_ITER; s++) {
            // Re-read compressed data from "image.bin"... (impractical in real scenario)
            int newLen = len + 4 * s;                   
        
            // Compress coefficients using Huffman coding algorithm...
            
            // Save compressed data into temp array
            for (size_t i = 0; i < newLen; i++) {
                tempData[i] = readCompressed("image.bin", &data);
            }
        }
        
        // Write new compressed data to file... ( implementation omitted )
    }
    
    // Release allocated memory
    free(huffmanCodedDCTCoefficients);

    return 0;
}
```
Note that this is a highly contrived example and not intended for actual deployment.