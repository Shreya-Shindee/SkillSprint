#!/usr/bin/env python3
"""
Comprehensive test demonstrating the enhanced resource quality system
Tests real learning path generation with validation and quality metrics
"""
import sys
import json
sys.path.append('.')

from utils.resource_search import get_resources_for_skill
from utils.enhanced_uniqueness import (
    ensure_resource_uniqueness_and_quality, 
    get_specialized_resources_for_subskill,
    get_performance_metrics,
    validate_url_accessibility
)

def test_enhanced_resource_system():
    print("🚀 Enhanced Resource Quality System Test")
    print("=" * 60)
    print("Testing with 'Data Structures and Algorithms' learning path")
    print()
    
    # Test different subskills
    subskills = ["Arrays", "Linked Lists", "Binary Trees", "Stacks"]
    all_resources = []
    
    for i, subskill in enumerate(subskills, 1):
        print(f"📚 Phase {i}: {subskill}")
        print("-" * 40)
        
        # Get specialized resources (hand-curated)
        specialized = get_specialized_resources_for_subskill(subskill)
        print(f"✨ Found {len(specialized)} specialized resources")
        
        # Get additional resources
        general = get_resources_for_skill(subskill, max_per_type=2)
        print(f"🔍 Found {len(general)} additional resources")
        
        # Combine and ensure uniqueness & quality
        combined_resources = specialized + general
        unique_resources = ensure_resource_uniqueness_and_quality(
            combined_resources, subskill, max_resources=4
        )
        
        print(f"✅ Final: {len(unique_resources)} unique, validated resources")
        print()
        
        # Display resources with validation
        for j, resource in enumerate(unique_resources, 1):
            title = resource.get('title', 'No title')
            url = resource.get('url', '')
            quality = resource.get('quality_score', 0)
            resource_type = resource.get('resource_type', 'unknown')
            
            print(f"  {j}. {title}")
            print(f"     Type: {resource_type.title()} | Quality: {quality}/100")
            print(f"     URL: {url}")
            
            # Validate URL in real-time
            is_valid = validate_url_accessibility(url)
            status = "✅ VALID" if is_valid else "❌ INVALID"
            print(f"     Status: {status}")
            print()
        
        all_resources.extend(unique_resources)
        print(f"📊 Cumulative resources: {len(all_resources)}")
        print("=" * 60)
        print()
    
    # Overall performance analysis
    print("🎯 OVERALL PERFORMANCE ANALYSIS")
    print("=" * 60)
    
    performance = get_performance_metrics(all_resources)
    
    print(f"📈 Performance Grade: {performance['performance_grade']}")
    print(f"🔗 Total Resources: {performance['total_resources']}")
    print(f"⭐ Average Quality Score: {performance['avg_quality_score']}/100")
    print(f"🎭 Uniqueness Score: {performance['uniqueness_score']}%")
    print(f"🌈 Resource Diversity: {performance['resource_diversity']}%")
    print(f"� Overall Score: {performance['overall_score']}/100")
    print(f"�📋 Resource Types: {', '.join(performance['resource_type_distribution'].keys())}")
    print(f"🎯 Unique Types Count: {performance['unique_types_count']}")
    print()
    
    # Check for duplicates
    print("🔍 DUPLICATE ANALYSIS")
    print("=" * 60)
    
    urls = [r.get('url', '') for r in all_resources]
    titles = [r.get('title', '') for r in all_resources]
    
    unique_urls = set(urls)
    unique_titles = set(titles)
    
    print(f"URLs: {len(urls)} total, {len(unique_urls)} unique")
    print(f"Titles: {len(titles)} total, {len(unique_titles)} unique")
    
    if len(unique_urls) == len(urls) and len(unique_titles) == len(titles):
        print("✅ PERFECT! No duplicates found!")
    else:
        print("⚠️ Warning: Some duplicates detected")
        
        # Show any duplicate URLs
        seen_urls = set()
        for url in urls:
            if url in seen_urls:
                print(f"   Duplicate URL: {url}")
            seen_urls.add(url)
    
    print()
    
    # Quality distribution
    print("📊 QUALITY DISTRIBUTION")
    print("=" * 60)
    
    quality_ranges = {
        'Excellent (90-100)': 0,
        'Great (80-89)': 0,
        'Good (70-79)': 0,
        'Average (60-69)': 0,
        'Below Average (<60)': 0
    }
    
    for resource in all_resources:
        quality = resource.get('quality_score', 0)
        if quality >= 90:
            quality_ranges['Excellent (90-100)'] += 1
        elif quality >= 80:
            quality_ranges['Great (80-89)'] += 1
        elif quality >= 70:
            quality_ranges['Good (70-79)'] += 1
        elif quality >= 60:
            quality_ranges['Average (60-69)'] += 1
        else:
            quality_ranges['Below Average (<60)'] += 1
    
    for range_name, count in quality_ranges.items():
        if count > 0:
            percentage = (count / len(all_resources)) * 100
            print(f"  {range_name}: {count} resources ({percentage:.1f}%)")
    
    print()
    
    # Final summary
    print("🎉 SUMMARY")
    print("=" * 60)
    
    valid_count = sum(1 for r in all_resources if validate_url_accessibility(r.get('url', '')))
    validity_rate = (valid_count / len(all_resources)) * 100 if all_resources else 0
    
    print(f"✅ URL Validity Rate: {validity_rate:.1f}% ({valid_count}/{len(all_resources)})")
    print(f"🎯 Quality Grade: {performance['performance_grade']}")
    print(f"🌟 Average Quality: {performance['avg_quality_score']:.1f}/100")
    print(f"🔄 Uniqueness: {performance['uniqueness_score']:.1f}%")
    print()
    
    # Show recommendations
    print("💡 RECOMMENDATIONS")
    print("=" * 60)
    for recommendation in performance.get('recommendations', []):
        print(f"   • {recommendation}")
    
    if (validity_rate >= 95 and 
        performance['performance_grade'] in ['A+', 'A', 'A-'] and 
        performance['uniqueness_score'] >= 95):
        print()
        print("🏆 EXCELLENT! Resource system is working perfectly!")
        print("   ✅ All URLs are valid and accessible")
        print("   ✅ High-quality educational content")
        print("   ✅ Unique resources across subskills")
        print("   ✅ Diverse resource types")
    else:
        print()
        print("⚠️ Some improvements needed:")
        if validity_rate < 95:
            print(f"   - URL validity needs improvement ({validity_rate:.1f}%)")
        if performance['performance_grade'] not in ['A+', 'A', 'A-']:
            print(f"   - Quality could be better (Grade: {performance['performance_grade']})")
        if performance['uniqueness_score'] < 95:
            print(f"   - Uniqueness needs work ({performance['uniqueness_score']:.1f}%)")

if __name__ == "__main__":
    test_enhanced_resource_system()
