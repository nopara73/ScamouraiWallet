package piuk.blockchain.android.util;

import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;

import org.apache.commons.io.IOUtils;

public class RandomOrgGenerator {
	public static byte[] getRandomBytes(int length) throws IOException {
		URL url = new URL("http://www.random.org/cgi-bin/randbyte?nbytes="+length+"&format=f");

		HttpURLConnection connection = (HttpURLConnection) url.openConnection();

		connection.setRequestMethod("GET");

		connection.setConnectTimeout(20000);
		connection.setReadTimeout(20000);

		connection.setInstanceFollowRedirects(false);

		connection.connect();
		
		return IOUtils.toByteArray(connection.getInputStream());
	}
	
}
