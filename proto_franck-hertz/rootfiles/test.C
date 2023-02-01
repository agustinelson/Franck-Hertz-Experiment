void test()
{
	TCanvas *c1 = new TCanvas();
	
	TGraphErrors *gr = new TGraphErrors();
	
	gr->SetTitle("Collector voltage: 7.00 V");
	gr->GetXaxis()->SetTitle("Acceleration voltage (V)");
	gr->GetYaxis()->SetTitle("Electric current (#muA)");
	
	
	fstream file;
	file.open("data/FH_7.00V.prn", ios::in);
	
	double x,y,ex,ey;
	
	int n = 0;
	
	while(1)
	{
		file >> x >> y >> ex >> ey;
		
		n = gr->GetN();
		
		gr->SetPoint(n, x, y);
		gr->SetPointError(n, ex, ey);
		
		if(file.eof()) break;
				
	}
	

	gr->Draw("ALP");
	
}
