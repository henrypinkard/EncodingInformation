from jax import jit
import jax.numpy as np

from encoding_information.models.model_base_class import MeasurementNoiseModel


class AnalyticGaussianNoiseModel(MeasurementNoiseModel):
    """
    Analytical model for estimating the conditional entropy H(Y | X) when the noise proces
    is additive independent Gaussian noise at each pixel.
    """
    
    def __init__(self, sigma):
        """        
        :param sigma: Standard deviation of the Gaussian noise
        """
        self.sigma = sigma

    def estimate_conditional_entropy(self):
        """
        Compute the conditional entropy H(Y | X) for Gaussian noise.
        """
        # Vectorize images
        images = images.reshape(-1, images.shape[-2] * images.shape[-1])
        
        # Conditional entropy H(Y | X) for Gaussian noise
        return 0.5 * np.log(2 * np.pi * np.e * self.sigma**2)

class PoissonNoiseModel(MeasurementNoiseModel):
    """
    Poisson noise model for estimating the conditional entropy H(Y | X) from empirical data.
    """

    def estimate_conditional_entropy(self, images):
        """
        images can be a train set or test set. Clean images are preferred.
        """
        # do the actual computation here
        images = images.reshape(-1, images.shape[-2] * images.shape[-1])
        n_pixels = images.shape[-1]
        
        # Conditional entropy H(Y | x) for Poisson noise
        gaussian_approx = 0.5 * (np.log(2 * np.pi * np.e) + np.log(images))
        gaussian_approx = np.where(images <= 0, 0, gaussian_approx)
        per_image_entropies = np.sum(gaussian_approx, axis=1) / n_pixels
        return np.mean(per_image_entropies) # h(y|x) per pixel
